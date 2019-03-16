from django.urls import path

from .views import department

app_name = 'dms'
urlpatterns = [
    path('', department.index, name='index'),
]