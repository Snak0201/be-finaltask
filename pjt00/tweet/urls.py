from django.urls import include, path
from . import views

app_name= 'tweet'

urlpatterns = [
    path('', views.tweet, name='tweet')
]
