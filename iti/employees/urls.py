from django.urls import path, include
import  employees.views
from employees.views import  employee_list, employees_index, delete_one, create_employee, edit_employee, employee_show

urlpatterns = [

    path('index', employees_index, name='employees.index'),
    path('index/<int:id>/delete', delete_one, name='employees.index'),
    path('create', create_employee, name='employees.create'),
    path('index/<int:id>', employee_show, name='employees.show'),

    path('edit/<int:id>', edit_employee, name='employees.edit'),
]