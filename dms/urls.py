from django.urls import path

from .views import department

app_name = 'dms'
urlpatterns = [
    # /dms/
    path('', department.index, name='index'),
    #
    path('<int:department_id>/', department.details, name='department_details_path'),
]