from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Department



# Create your views here.

def index(request):
    departments_list = Department.objects.all()
    context = { 'departments_list' : departments_list}

    return render(request, context=context, template_name='index')