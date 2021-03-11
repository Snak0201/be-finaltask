from django.urls import path
from . import views

app_name= 'tclone'

urlpatterns = [
    path('', views.top, name='top'),
    path('entry/', views.EntryUserView.as_view(), name='entry'),
    path('entry/ok', views.ok, name='entryok'),
]
