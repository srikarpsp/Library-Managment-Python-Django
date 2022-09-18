from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

# django hosts --> subdomain for reverse
class BookType(models.Model):
    Types = models.CharField(max_length=50)
    

    def __str__(self):
        return self.Types

class Book(models.Model):
    # pk aka id --> numbers
    BookId      = models.AutoField(primary_key=True)
    Types       = models.ForeignKey(BookType, null=True, on_delete=models.CASCADE)
    BookName    = models.CharField(max_length=120, null=True, blank=True)
    Author      = models.CharField(max_length=120, null=True, blank=True)
    Publication = models.CharField(max_length=120, null=True, blank=True)
    Published   = models.CharField(max_length=120, null=True, blank=True)
    def __str__(self):
        return self.BookName


   # @property
    #def owner(self):
     #   return self.types

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    
    #def get_api_url(self, request=None):
     #   return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)