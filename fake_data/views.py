from django.contrib.auth import (login as auth_login,  authenticate)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import DataSchema, DataSet, Field
from .forms import FieldFormset, DataSchemaForm


def login(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'login/login.html', context)

@login_required
def list_schema(request):
    schemas = DataSchema.objects.all()
    return render(request, 'fake_data/list_schema.html', {'schemas': schemas})

@login_required
def new_schema(request):
    if request.method == "POST":
        dataschema_form = DataSchemaForm(request.POST)
        if dataschema_form.is_valid():
            schema = dataschema_form.save()
        field_formset = FieldFormset(request.POST, instance=schema)
        if field_formset.is_valid():
            field_formset.save()
            return redirect('list_dataset', id=schema.id)
    else:
        dataschema_form = DataSchemaForm()
        field_formset = FieldFormset()
    return render(request, 'fake_data/edit_schema.html', {'field_formset': field_formset, 'dataschema_form': dataschema_form})


@login_required
def edit_schema(request, id):
    schema = DataSchema.objects.get(id=id)
    if request.method == "POST":
        dataschema_form = DataSchemaForm(request.POST, instance=schema)
        if dataschema_form.is_valid():
            schema = dataschema_form.save()
        field_formset = FieldFormset(request.POST, instance=schema)
        if field_formset.is_valid():
            field_formset.save()
            return redirect('list_dataset', id=schema.id)
    else:
        dataschema_form = DataSchemaForm(instance=schema)
        field_formset = FieldFormset(instance=schema)
    return render(request, 'fake_data/edit_schema.html', {'field_formset': field_formset, 'dataschema_form': dataschema_form})

@login_required
def list_dataset(request, id):
    schema = DataSchema.objects.get(id=id)
    datasets = DataSet.objects.filter(schema=schema)
    return render(request, 'fake_data/list_dataset.html', {'schema': schema, 'datasets': datasets})


@login_required
def delete_schema(request, id):
    schema = DataSchema.objects.get(id=id)
    schema.delete()
    return redirect('list_schema')