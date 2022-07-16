import re
from django.shortcuts import render
from Employee.models import Employee
from django.db import connection
# Create your views here.

def empHome(request):
    return render(request, 'EmployeeHome.html')


def Create(request):
    return render(request, 'Create.html')


def CreateResult(request):
    try:
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        designation = request.POST.get('designation')
        salary = request.POST.get('salary')
    
        emp = Employee(empFirstName=firstName, empLastName=lastName, empDesignation=designation, empSalary=salary)
        emp.save()

        '''query = "INSERT INTO Employee_employee(empFirstName, empLastName, empDesignation, empSalary, empDoj) "\
                "VALUES('"+firstName+"', '"+lastName+"', '"+designation+"', '"+salary+"', '2022-07-13');"
        with connection.cursor() as cursor:
            cursor.execute(query)'''
        return render(request, 'Success.html')
    except Exception as e:
        return render(request, 'Error.html', {'exception': str(e)})


def Read(request):
    return render(request, 'Read.html')


def ReadResult(request):
    try:
        empId = request.POST.get('empId', '')
        action = request.POST.get('checkbox', 'off')
        if action == 'all':
            # employees = Employee.objects.all()
            employees = Employee.objects.raw('Select * from Employee_employee')
            return render(request, 'ReadSuccess.html', {'Employees': employees})
        elif action == 'getById' and empId is not '':
            employees = Employee.objects.filter(empId=empId)
            if len(employees) == 0:
                return render(request, 'Error.html', {'exception': 'No employee found with this employee Id'})    
            return render(request, 'ReadSuccess.html', {'Employees': employees}) 
        else:
            return render(request, 'Error.html', {'exception': 'Invalid Selection!'})
    except Exception as e:
        return render(request, 'Error.html', {'exception': str(e)})


def Update(request):
    return render(request, 'Update.html')


def UpdateResult(request):
    try:
        empId = request.POST.get('empId', '')
        firstName = request.POST.get('firstName', '')
        lastName = request.POST.get('lastName', '')
        designation = request.POST.get('designation', '')
        salary = request.POST.get('salary', '')
    
        with connection.cursor() as cursor:
            query = f"UPDATE Employee_employee SET empFirstName = '{firstName}', empLastName = '{lastName}', "\
                    f"empDesignation = '{designation}', empSalary = '{salary}' WHERE empId = '{empId}'"
            cursor.execute(query)
        return render(request, 'Success.html')
    except Exception as e:
        return render(request, 'Error.html', {'exception': str(e)})


def Delete(request):
    return render(request, 'Delete.html')


def DeleteResult(request):
    try:
        empId = request.POST.get('empId', '')
        emp = Employee.objects.get(empId=empId)
        emp.delete()
        return render(request, 'Success.html')
    except Exception as e:
        return render(request, 'Error.html', {'exception': str(e)})
