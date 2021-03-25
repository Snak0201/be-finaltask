from django.urls import include, path
from . import views

app_name= 'tweet'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet/<int:pk>/', views.tdetail, name='tdetail'),
    path('tweet/<int:pk>/edit/', views.tedit, name='tedit'),
    path('tweet/<int:pk>/delete', views.tdelete, name='tdelete'),
]
