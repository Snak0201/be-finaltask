from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView


class TopView(TemplateView):
    template_name = 'tclone/top.html'

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
            return super().form_valid(form)
        else:
            return(reverse_lazy('tclone:top'))

class EntryOKView(TemplateView):
    template_name = 'tclone/entryok.html'

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'tclone/home.html'
