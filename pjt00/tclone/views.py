from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DeleteView ,FormView, TemplateView
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
            form.add_error(None,'なぜかあなた自身をフォローしようとしています')
            return super().form_invalid(form)
        elif FF.objects.filter(user=model.user, followed=model.followed).exists():
            form.add_error(None,'もうフォロー済みです')
            return super().form_invalid(form)
        else:
            model.save()
        return super().form_valid(form)

@require_POST
@login_required
def followx(request, pk):
    user = get_user_model().objects.get(pk=request.user.pk)
    followed = get_user_model().objects.get(pk=pk)
    ff = FF.objects.filter(
        user = user,
        followed = followed
    )
    ff.delete()
    messages.success(request, 'フォローを解除しました')
    return redirect('tweet:home')


# class FollowXView(LoginRequiredMixin, DeleteView):
#     model = FF
#     template_name = 'tclone/followx.html'
#     success_url = reverse_lazy('tweet:home')
#     def delete(self, request, pk):
#         user = get_user_model().objects.get(pk=request.user.pk)
#         followed = get_user_model().objects.get(pk=pk)
#         ff = FF.objects.filter(
#             user = user,
#             followed = followed
#         )
#         if user == followed:
#             messages.error(self.request, 'なぜかあなた自身をフォロー解除しようとしています')
#         ff.delete()
#         messages.success(self.request, 'フォローを解除しました')
#         return super().delete(request)
