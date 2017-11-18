from django.http import HttpResponse
from django.shortcuts import render

from .models import Employee, Key, Keycode

def index(request):
    employeelist = Employee.objects.order_by('-first_name')[:5]
    context = {'employeelist': employeelist}
    return render(request, 'keymanage/index.html', context)

def detail(request, employee_id):
    return HttpResponse("You're looking at employee %s." % employee_id)

def detail(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    codes = Keycode.objects.all
    keylist = Key.objects.filter(assignee=employee_id)
    context = {'employee': employee, 'keylist': keylist, 'codes': codes}
    return render(request, 'keymanage/details.html', context)