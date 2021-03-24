from django.urls import include, path
from . import views

app_name= 'tweet'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tweet/', views.tweet, name='tweet'),
    path('detail/tweetid=<int:pk>/', views.detail, name='detail'),
]
