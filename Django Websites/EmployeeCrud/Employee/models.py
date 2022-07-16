import datetime
from django.db import models


class Employee(models.Model):
    empId = models.AutoField(primary_key=True)
    empFirstName = models.CharField(max_length=30)
    empLastName = models.CharField(max_length=30)
    empDesignation = models.CharField(max_length=30)
    empSalary = models.FloatField()
    empDoj = models.DateField(default=datetime.datetime.today)

    def __str__(self) -> str:
        return f'Employee object with employee id = {self.empId} and employee name = {self.empFirstName} {self.empLastName}'
