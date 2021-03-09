from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

# Create your views here.
class CreateUser(FormView):
    form_class = UserCreationForm
    template_name = 'tclone/entry.html'
    success_url = reverse_lazy('tclone:ok')
    def form_valid(self, form):
        status = self.request.post['judge']
        if status == 'judge':
            return render(request, 'tclone/ok.html')

def top(request):
    return render(request, 'tclone/top.html')

def entry(request):
    return render(request, 'tclone/entry.html')

def entryconfirm(request):
    return render(request, 'tclone/entryconf.html')

def ok(request):
    return render(request, 'tclone/ok.html')
