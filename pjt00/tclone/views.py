from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView
from .forms import FollowXForm
from .models import FF


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

class FollowView(LoginRequiredMixin, CreateView):
    model = FF
    fields = []
    template_name = 'tclone/follow.html'
    success_url = reverse_lazy('tweet:home')
    def form_valid(self, form):
        model = form.save(commit=False)
        model.user = get_user_model().objects.get(pk=self.request.user.id)
        model.followed = get_object_or_404(
            get_user_model(),
            pk=self.kwargs['pk']
            )
        if model.user == model.followed:
            form.add_error(None,'もうフォロー済みです')
            return super().form_invalid(form)
        elif FF.objects.filter(user=model.user, followed=model.followed).exists():
            form.add_error(None,'もうフォロー済みです')
            return super().form_invalid(form)
        else:
            model.save()
        return super().form_valid(form)

class FollowXView(FormView):
    form_class = FollowXForm
    template_name = 'tclone/followx.html'
    success_url = reverse_lazy('tclone:followx')
