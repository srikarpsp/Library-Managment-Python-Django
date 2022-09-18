# generic

#from django.db.models import Q
from rest_framework import viewsets
from django.shortcuts import render
from Employee_Registration.models import Employee
#from .permissions import IsOwnerOrReadOnly
from .serializers import EmployeeSerializer


class EmployeeView(viewsets.ModelViewSet): # DetailView CreateView FormView
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer     

# class EmployeenameView(viewsets.ModelViewSet):
# 	queryset = Employeename.objects.all()
# 	serializer_class = EmployeenameSerializer