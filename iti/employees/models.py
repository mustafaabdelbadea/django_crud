from django.db import models
from  django.shortcuts import  reverse
from department.models import Department
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    salary = models.IntegerField(null=False)
    dept = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE, related_name='dept_employees')

    @classmethod
    def get_all_employees(cls):
        return cls.objects.all()

    @classmethod 
    def get_employee(cls, id):
        return cls.objects.get(id = id)
    
    def get_delete_url(self):
        delete_url = reverse('employees.index', args = [self.id])
        return delete_url

    def get_show_url(self):
        show_url = reverse('employees.show',args=[self.id])
        return show_url
    
    def get_edit_url(self):
        edit_url = reverse('employees.edit',args=[self.id])
        return edit_url