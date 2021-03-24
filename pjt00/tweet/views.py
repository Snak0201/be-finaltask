from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from .forms import TweetForm
from .models import Tweet


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'tweet/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tweets'] = Tweet.objects.all()
        return context

@login_required
def tweet(request):
    form = TweetForm(request.POST)
    if request.method == 'POST':
        check = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet:home')
    else:
        form = TweetForm()
    return render(request, 'tweet/tweet.html', {'form': form})
