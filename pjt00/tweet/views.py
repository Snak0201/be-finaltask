from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView,TemplateView, View
from rules.contrib.views import permission_required, objectgetter
from .forms import TweetForm
from .models import Tweet, Favorite
from tclone.models import FF


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'tweet/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tweets'] = Tweet.objects.all()
        return context

@login_required
def tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
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

@permission_required('tweet.can_tedit',fn=objectgetter(Tweet, 'pk'))
def tedit(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            tweet.save()
            return redirect('tweet:home')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet/tweet.html', {'form': form})

@require_POST
@permission_required('tweet.can_tedit',fn=objectgetter(Tweet, 'pk'))
def tdelete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    tweet.delete()
    return redirect('tweet:home')

@login_required
def profile(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    tweets = Tweet.objects.filter(user=user)
    ff = FF.objects.filter(user=request.user, followed=user)
    return render(request, 'tweet/profile.html',
        {
        'user': user,
        'tweets': tweets,
        'ff': ff
        }
    )

class FavoriteView(LoginRequiredMixin, CreateView):
    model = Favorite
    fields = []
    template_name = 'tweet/favorite.html'
    success_url = reverse_lazy('tweet:home')
    def form_valid(self, form):
        model = form.save(commit=False)
        model.user = get_user_model().objects.get(pk=self.request.user.id)
        model.tweet = get_object_or_404(
            Tweet,
            pk = self.kwargs['pk']
            )
        return super().form_valid(form)

class FavoriteDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        user = get_user_model().objects.get(pk=request.user.pk)
        tweet = get_object_or_404(Tweet, pk=pk)
        favorite = Favorite.objects.filter(
            user = user,
            tweet = tweet
            )
        favorite.delete()
        return redirect('tweet:home')