from django.contrib import admin
from django.urls import path, include
# from students.views import helloworld
from department.views import  departments_index, show_dept, delete_dept
urlpatterns = [
    path('', departments_index, name='departments.index'),
    path('<int:dept_id>',show_dept, name='departments.show'),
path('<int:dept_id>/delete',delete_dept, name='departments.delete'),

]