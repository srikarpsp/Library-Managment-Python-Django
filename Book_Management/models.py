from django.conf import settings
from django.db import models
from django.urls import reverse
from library_management.models import Book
from Employee_Registration.models import Employee
from rest_framework.reverse import reverse as api_reverse

# django hosts --> subdomain for reverse
# class Employeename(models.Model):
#     employeename = models.CharField(max_length=50, null=True, blank=True)
    
#     def __str__(self):
#         return self.employeename            

# class Bookname(models.Model):
#     bookname = models.CharField(max_length=50, null=True, blank=True)

#     def __str__(self):
#         return self.bookname

class Assignbook(models.Model):
    # pk aka id --> numbers
    Employeeid   = models.ForeignKey(Employee, related_name="custom_Employeeid_profile", on_delete=models.CASCADE, blank=True)
    # employeename = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE, blank=True)
    # BookName     = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    BookId       = models.ForeignKey(Book, related_name="custom_BookId_profile", on_delete=models.CASCADE, blank=True)
    issue        = models.DateField()
    renew        = models.DateField()
    # issue        = models.CharField(max_length=120, null=True, blank=True)
    # renew        = models.CharField(max_length=120, null=True, blank=True)
    
    #  def __str__(self):
    #     return self.BookName

class Bookdetails(models.Model):
    Employeeid         = models.CharField(max_length=120, null=True, blank=True)
    assignbook         = models.ManyToManyField(Book, related_name="custom_Employeeid_profile") 
      # def __str__(self):
      #     return str(self.BookName)

   # @property
    #def owner(self):
     #   return self.types

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    
    #def get_api_url(self, request=None):
     #   return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)