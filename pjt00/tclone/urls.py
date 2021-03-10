from django.urls import path
from . import views

app_name= 'tclone'

urlpatterns = [
    path('', views.top, name='top'),
    path('entry/', views.EntryUser.as_view(), name='entry'),
    # path('entry/confirm', views.entryconfirm, name='entryconfirm'),
    path('entry/ok', views.ok, name='entryok'),
]
