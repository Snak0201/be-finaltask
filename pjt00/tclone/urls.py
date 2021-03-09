from django.urls import path
from . import views


urlpatterns = [
    path('', views.top, name='top'),
    path('entry/', views.entry, name='entry'),
    path('entry/confirm', views.entryconfirm, name='entryconfirm'),
    path('entry/ok', views.ok, name='entryok'),
]
