from django.contrib.auth import (login as auth_login,  authenticate)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import DataSchema, DataSet, Field


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
    context = {}
    return render(request, 'fake_data/list_schema.html', context)

@login_required
def new_schema(request):
    context = {}
    return render(request, 'fake_data/new_schema.html', context)

@login_required
def list_dataset(request, id):
    schema = DataSchema.objects.get(id=id)
    context = {}
    return render(request, 'fake_data/list_dataset.html', context)