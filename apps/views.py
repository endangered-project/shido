from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect

from apps.forms import ClassForm, InstanceForm, InstanceInstanceConnectionForm, PropertyTypeForm, \
    ObjectPropertyStringForm, ObjectPropertyNumberForm, ObjectPropertyFloatForm, ObjectPropertyBooleanForm, \
    ObjectPropertyDateForm, ObjectPropertyDateTimeForm, ObjectPropertyMarkdownForm, ObjectPropertyImageForm, \
    ObjectPropertyFileForm, ObjectPropertyInstanceForm, ObjectPropertyInstanceListForm
from apps.models import Class, Instance, InstanceInstanceConnection, PropertyType, type_limitation_template, \
    ObjectPropertyRelation
from apps.templatetags.json_to_list import json_to_list


def home(request):
    return render(request, 'apps/home.html')


def class_list(request):
    return render(request, 'apps/class/list.html', {
        'all_class': Class.objects.all()
    })


@login_required()
def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Class created successfully!')
            return redirect('apps_class_list')
    else:
        form = ClassForm()
    return render(request, 'apps/class/create.html', {
        'form': form
    })


def class_detail(request, class_id):
    if not Class.objects.filter(id=class_id).exists():
        messages.error(request, f'Class with id {class_id} does not exist')
        return redirect('apps_class_list')
    return render(request, 'apps/class/detail.html', {
        'class': Class.objects.get(id=class_id)
    })


@login_required()
def class_edit(request, class_id):
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=Class.objects.get(id=class_id))
        if form.is_valid():
            form.save()
            messages.success(request, f'Class edited successfully!')
            return redirect('apps_class_detail', class_id=class_id)
    else:
        form = ClassForm(instance=Class.objects.get(id=class_id))
    return render(request, 'apps/class/edit.html', {
        'form': form,
        'class': Class.objects.get(id=class_id)
    })


def instance_list(request):
    return render(request, 'apps/instances/list.html', {
        'all_instances': Instance.objects.all(),
        'all_classes': Class.objects.all()
    })


@login_required()
def instance_create(request):
    if request.method == 'POST':
        form = InstanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Instance created successfully!')
            return redirect('apps_instance_list')
    else:
        form = InstanceForm()
    return render(request, 'apps/instances/create.html', {
        'form': form
    })


def instance_detail(request, instance_id):
    if not Instance.objects.filter(id=instance_id).exists():
        messages.error(request, f'Instance with id {instance_id} does not exist')
        return redirect('apps_instance_list')
    return render(request, 'apps/instances/detail.html', {
        'instance': Instance.objects.get(id=instance_id),
        'object_property': ObjectPropertyRelation.objects.filter(instance_object_id=instance_id)
    })


@login_required()
def instance_edit(request, instance_id):
    if request.method == 'POST':
        form = InstanceForm(request.POST, instance=Instance.objects.get(id=instance_id))
        if form.is_valid():
            form.save()
            messages.success(request, f'Instance edited successfully!')
            return redirect('apps_instance_detail', instance_id=instance_id)
    else:
        form = InstanceForm(instance=Instance.objects.get(id=instance_id))
    return render(request, 'apps/instances/edit.html', {
        'form': form,
        'instance': Instance.objects.get(id=instance_id)
    })


@login_required()
def instance_add_property_list(request, instance_id):
    try:
        instance = Instance.objects.get(id=instance_id)
    except Instance.DoesNotExist:
        messages.error(request, f'Instance with id {instance_id} does not exist')
        return redirect('apps_instance_list')
    property_list = []
    for property_type in PropertyType.objects.filter(class_instance=instance.class_instance):
        property_list.append({
            'property_type': property_type,
            'exist': ObjectPropertyRelation.objects.filter(instance_object=instance, property_type=property_type).exists()
        })
    return render(request, 'apps/instances/add_property_list.html', {
        'instance': instance,
        'all_property_types': property_list
    })


@login_required
def instance_add_property_form(request, instance_id, property_type_id):
    try:
        instance = Instance.objects.get(id=instance_id)
    except Instance.DoesNotExist:
        messages.error(request, f'Instance with id {instance_id} does not exist')
        return redirect('apps_instance_list')
    try:
        property_type = PropertyType.objects.get(id=property_type_id)
    except PropertyType.DoesNotExist:
        messages.error(request, f'Property type with id {property_type_id} does not exist')
        return redirect('apps_instance_list')
    if request.method == 'POST':
        if property_type.raw_type == 'string':
            form = ObjectPropertyStringForm(request.POST, max_length=property_type.limitation['max_length'], min_length=property_type.limitation['min_length'], initial_value='')
        elif property_type.raw_type == 'number':
            form = ObjectPropertyNumberForm(request.POST, min_value=property_type.limitation['min_value'], max_value=property_type.limitation['max_value'], initial_value=property_type.limitation['min_value'])
        elif property_type.raw_type == 'float':
            form = ObjectPropertyFloatForm(request.POST, min_value=property_type.limitation['min_value'], max_value=property_type.limitation['max_value'], decimal_places=property_type.limitation['decimal_places'], initial_value=property_type.limitation['min_value'])
        elif property_type.raw_type == 'boolean':
            form = ObjectPropertyBooleanForm(request.POST, initial_value=False)
        elif property_type.raw_type == 'date':
            form = ObjectPropertyDateForm(request.POST, initial_value='2020-01-01')
        elif property_type.raw_type == 'datetime':
            form = ObjectPropertyDateTimeForm(request.POST, initial_value='2020-01-01 00:00:00')
        elif property_type.raw_type == 'markdown':
            form = ObjectPropertyMarkdownForm(request.POST, request.FILES, initial_value='')
        elif property_type.raw_type == 'image':
            form = ObjectPropertyImageForm(request.POST, request.FILES)
        elif property_type.raw_type == 'file':
            form = ObjectPropertyFileForm(request.POST, request.FILES)
        elif property_type.raw_type == 'instance':
            form = ObjectPropertyInstanceForm(request.POST, class_id=property_type.limitation['class_id'], initial_value=Instance.objects.filter(class_instance_id=property_type.limitation['class_id']).first())
        elif property_type.raw_type == 'instance_list':
            form = ObjectPropertyInstanceListForm(request.POST, class_id_list=property_type.limitation['allow_class_id_list'], initial_value=[])
        else:
            messages.error(request, f'Raw type {property_type.raw_type} is not supported for adding property')
            return redirect('apps_instance_detail', instance_id=instance_id)
        if form.is_valid():
            if property_type.raw_type == 'image' or property_type.raw_type == 'file':
                # save file to media
                file = form.cleaned_data['value']
                file_name = default_storage.save(f'apps/{property_type.raw_type}/{file.name}', file)
                # get path to file, not full path, only path from media
                file_path = default_storage.url(file_name)
                raw_value = file_path
            elif property_type.raw_type == 'instance_list':
                # get list of instance id with comma separated
                raw_value = ','.join([str(instance.id) for instance in form.cleaned_data['value']])
            elif property_type.raw_type == 'instance':
                raw_value = str(form.cleaned_data['value'].id)
            else:
                raw_value = form.cleaned_data['value']
            ObjectPropertyRelation.objects.create(
                instance_object=instance,
                property_type=property_type,
                raw_value=raw_value
            )
            messages.success(request, f'Property added successfully!')
            return redirect('apps_instance_detail', instance_id=instance_id)
    else:
        if property_type.raw_type == 'string':
            form = ObjectPropertyStringForm(max_length=property_type.limitation['max_length'], min_length=property_type.limitation['min_length'], initial_value='')
        elif property_type.raw_type == 'number':
            form = ObjectPropertyNumberForm(min_value=property_type.limitation['min_value'], max_value=property_type.limitation['max_value'], initial_value=property_type.limitation['min_value'])
        elif property_type.raw_type == 'float':
            form = ObjectPropertyFloatForm(min_value=property_type.limitation['min_value'], max_value=property_type.limitation['max_value'], decimal_places=property_type.limitation['decimal_places'], initial_value=property_type.limitation['min_value'])
        elif property_type.raw_type == 'boolean':
            form = ObjectPropertyBooleanForm(initial_value=False)
        elif property_type.raw_type == 'date':
            form = ObjectPropertyDateForm(initial_value='2020-01-01')
        elif property_type.raw_type == 'datetime':
            form = ObjectPropertyDateTimeForm(initial_value='2020-01-01 00:00:00')
        elif property_type.raw_type == 'markdown':
            form = ObjectPropertyMarkdownForm(initial_value='')
        elif property_type.raw_type == 'image':
            form = ObjectPropertyImageForm()
        elif property_type.raw_type == 'file':
            form = ObjectPropertyFileForm()
        elif property_type.raw_type == 'instance':
            form = ObjectPropertyInstanceForm(class_id=property_type.limitation['class_id'], initial_value=Instance.objects.filter(class_instance_id=property_type.limitation['class_id']).first())
        elif property_type.raw_type == 'instance_list':
            form = ObjectPropertyInstanceListForm(class_id_list=property_type.limitation['allow_class_id_list'], initial_value=[])
        else:
            messages.error(request, f'Raw type {property_type.raw_type} is not supported for adding property')
            return redirect('apps_instance_detail', instance_id=instance_id)
    return render(request, 'apps/instances/add_property_form.html', {
        'form': form,
        'instance': instance,
        'property_type': property_type,
        'limitation_list': json_to_list(property_type.limitation)
    })


def instance_instance_connection_list(request):
    return render(request, 'apps/instance_instance_connection/list.html', {
        'all_instances': InstanceInstanceConnection.objects.all()
    })


@login_required()
def instance_instance_connection_create(request):
    if request.method == 'POST':
        form = InstanceInstanceConnectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Instance-Instance Connection created successfully!')
            return redirect('apps_instance_instance_connection_list')
    else:
        form = InstanceInstanceConnectionForm()
    return render(request, 'apps/instance_instance_connection/create.html', {
        'form': form
    })


def instance_instance_connection_detail(request, instance_instance_connection_id):
    if not InstanceInstanceConnection.objects.filter(id=instance_instance_connection_id).exists():
        messages.error(request, f'Instance-Instance Connection with id {instance_instance_connection_id} does not exist')
        return redirect('apps_instance_instance_connection_list')
    return render(request, 'apps/instance_instance_connection/detail.html', {
        'instance_instance_connection': InstanceInstanceConnection.objects.get(id=instance_instance_connection_id)
    })


def property_type_list(request):
    return render(request, 'apps/property_type/list.html', {
        'all_property_type': PropertyType.objects.all()
    })


@login_required()
def property_type_create(request):
    if request.method == 'POST':
        form = PropertyTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Property type created successfully!')
            return redirect('apps_property_type_list')
    else:
        form = PropertyTypeForm()
    return render(request, 'apps/property_type/create.html', {
        'form': form
    })


def property_type_detail(request, property_type_id):
    if not PropertyType.objects.filter(id=property_type_id).exists():
        messages.error(request, f'Property type with id {property_type_id} does not exist')
        return redirect('apps_property_type_list')
    property_type = PropertyType.objects.get(id=property_type_id)
    return render(request, 'apps/property_type/detail.html', {
        'property_type': property_type,
        'limitation_list': json_to_list(property_type.limitation)
    })
