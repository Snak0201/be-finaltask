from django.urls import include, path
from . import views

app_name= 'tclone'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('', include('django.contrib.auth.urls')),
    path('entry/', views.EntryUserView.as_view(), name='entry'),
    path('entry/ok', views.EntryOKView.as_view(), name='entryok'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/tweet', views.TweetView.as_view(), name='tweet')
    ]
