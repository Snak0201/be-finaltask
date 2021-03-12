from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

# Create your views here.
class EntryUserView(FormView):
    form_class = UserCreationForm
    template_name = 'tclone/entry.html'
    success_url = reverse_lazy('tclone:entryok')
    def form_valid(self, form):
        status = self.request.POST['proceed']
        if status == 'go':
            return render(self.request, 'tclone/entryconfirm.html', {'form': form})
        elif status == 'judge':
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            return super().form_valid(form)
        else:
            return(reverse_lazy('tclone:top'))


def top(request):
    return render(request, 'tclone/top.html')

def ok(request):
    return render(request, 'tclone/entryok.html')

def login(request):
    return render(request, 'tclone/login.html')

def home(request):
    return render(request, 'tclone/home.html')
