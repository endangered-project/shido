from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.forms import ClassForm, InstanceForm
from apps.models import Class, Instance


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
