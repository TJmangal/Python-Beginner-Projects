from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.empHome, name='empHome'),
    path('/Create', views.Create, name='Create'),
    path('/CreateResult', views.CreateResult, name='CreateResult'),
    path('/Read', views.Read, name='Read'),
    path('/ReadResult', views.ReadResult, name='ReadResult'),
    path('/Update', views.Update, name='Update'),
    path('/UpdateResult', views.UpdateResult, name='UpdateResult'),
    path('/Delete', views.Delete, name='Delete'),
    path('/DeleteResult', views.DeleteResult, name='DeleteResult')
]
