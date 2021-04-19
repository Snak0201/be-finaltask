from django.urls import path
from . import views

app_name= 'tweet'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet/<int:pk>/', views.tdetail, name='tdetail'),
    path('tweet/<int:pk>/edit/', views.tedit, name='tedit'),
    path('tweet/<int:pk>/delete/', views.tdelete, name='tdelete'),
    path('tweet/<int:pk>/favorite/', views.FavoriteView.as_view(), name='favorite'),
    path('tweet/<int:pk>/favorite/delete', views.FavoriteDeleteView.as_view(), name='fdelete'),
]
