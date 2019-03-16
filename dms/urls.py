from django.urls import path

from . import views

app_name = 'dms'
urlpatterns = [
    path('', views.index, name='index'),
]