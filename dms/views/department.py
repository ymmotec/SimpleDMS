from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from dms.models import Department



# Create your views here.

def index(request):
    departments_list = Department.objects.all()
    context = { 'departments_list' : departments_list}

    return render(request, 'dms/index.html', context)


def details(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'dms/department_details.html', {'department': department})