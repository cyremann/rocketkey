from django.shortcuts import render

from .models import Employee


def index(request):
    employeelist = Employee.objects.order_by('-first_name')[:5]
    context = {'employeelist': employeelist}
    return render(request, 'keymanage/index.html', context)