# generic

#from django.db.models import Q
from rest_framework import viewsets
from django.shortcuts import render
from Book_Management.models import Assignbook, Bookdetails
from library_management.models import Book
from Employee_Registration.models import Employee
#from .permissions import IsOwnerOrReadOnly
from .serializers import AssignbookSerializer, BookSerializer, EmployeeSerializer, BookdetailsSerializer


class AssignbookView(viewsets.ModelViewSet): # DetailView CreateView FormView
   queryset = Assignbook.objects.all()
   serializer_class = AssignbookSerializer     

class EmployeeView(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class BookView(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class BookdetailsView(viewsets.ModelViewSet):
	queryset = Bookdetails.objects.all()
	serializer_class = BookdetailsSerializer




