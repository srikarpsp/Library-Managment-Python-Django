
# Create your views here.
# generic

#from django.db.models import Q
from rest_framework import viewsets
from django.shortcuts import render
from .models import Book, BookType
#from .permissions import IsOwnerOrReadOnly
from .serializers import BookSerializer, BookTypeSerializer



class BookView(viewsets.ModelViewSet): # DetailView CreateView FormView
   queryset = Book.objects.all()
   serializer_class = BookSerializer     

class BookTypeView(viewsets.ModelViewSet): # DetailView CreateView FormView
   queryset = BookType.objects.all()
   serializer_class = BookTypeSerializer

