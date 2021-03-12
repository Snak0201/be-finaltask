from django.urls import include, path
from . import views

app_name= 'tclone'

urlpatterns = [
    path('', views.top, name='top'),
    path('', include('django.contrib.auth.urls'), name='login'),
    path('entry/', views.EntryUserView.as_view(), name='entry'),
    path('entry/ok', views.ok, name='entryok'),
    path('home/', views.home, name='home'),
    ]
