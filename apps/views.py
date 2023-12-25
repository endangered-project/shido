from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.forms import ClassForm, InstanceForm, InstanceInstanceConnectionForm
from apps.models import Class, Instance, InstanceInstanceConnection


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
        'all_instances': Instance.objects.all()
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
    return render(request, 'apps/instances/detail.html', {
        'instance': Instance.objects.get(id=instance_id)
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
    return render(request, 'apps/instance_instance_connection/detail.html', {
        'instance_instance_connection': InstanceInstanceConnection.objects.get(id=instance_instance_connection_id)
    })