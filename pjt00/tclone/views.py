from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.


def entry(request):
    return render(request, 'tclone/entry.html')
