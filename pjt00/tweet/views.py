from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
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

@login_required
def tdetail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    return render(request, 'tweet/tdetail.html', {'tweet': tweet})

@login_required
def tedit(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            tweet.save()
            return redirect('tweet:home', pk=tweet.pk)
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet/tweet.html', {'form': form})

@require_POST
def tdelete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    tweet.delete()
    return redirect('tweet:home')
