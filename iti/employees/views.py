from django.shortcuts import render, redirect, reverse
from  django.http import HttpResponse
from employees.models import Employee
from employees.forms import  EmployeeForm


employees = ['Ahmed', 'Mohamed', 'Mustafa']
def allEmployees(request):
    return HttpResponse(employees)


def getEmployee(request, id):
    # return HttpResponse(id)
    if id in range(len(employees)):
        return HttpResponse(employees[id])
    else:
        return HttpResponse("<h1> Employee not found </h1>")


def landingpage(request):
    return render(request, 'landing.html')



def employee_list(request):
    return render(request,'list.html',context={"allEmployees": employees}  )

def employees_index(request):
    employees = Employee.get_all_employees()
    return render(request, 'employees/index.html', context={"employees": employees})

def delete_one(request, id):
    employee = Employee.get_employee(id)
    employee.delete()
    redirect_url = reverse('employees.index')
    return redirect(redirect_url)

def create_employee(request):
    if request.method == 'GET':
        return render(request, 'employees/create.html')
    else:
        return HttpResponse(("POST "))

def employee_show(request, id):
    # employees= employee.objects.all()
    employee = Employee.get_employee(id)
    return render(request, 'employees/show.html', context={"employee":employee})


def create_employee(request):
    form  = EmployeeForm()
    if request.method =='GET':
        return render(request, 'employees/create.html', context={"form":form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        redirect_url = reverse('employees.index')
        return redirect(redirect_url)


def edit_employee(request, id):
    employee = Employee.get_employee(id)
    if request.method =='GET':
        form  = EmployeeForm(instance=employee)
        return render(request, 'employees/edit.html', context={"form":form})
    else:
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        redirect_url = reverse('employees.index')
        return redirect(redirect_url)