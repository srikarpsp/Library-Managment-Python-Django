from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

#django hosts --> subdomain for reverse
# class Employeename(models.Model):
#     employeename = models.CharField(max_length=50, null=True, blank=True)
    

#     def __str__(self):
#         return self.employeename

class Employee(models.Model):
    # pk aka id --> numbers
    #user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    Employeeid  = models.AutoField(primary_key=True)
    employeename = models.CharField(max_length=120, null=True, blank=True)
    contact     = models.CharField(max_length=120, null=True, blank=True)
    email       = models.CharField(max_length=120, null=True, blank=True)
    DEPARTMENT_CHOICES = (
        ('Sales & marketing','Sales & marketing'),
        ('Webapp Associate','Webapp Associate'),
        ('Webapp Architect','Webapp Architect'),
        ('Webapp Engineer','Webapp Engineer'),
        ('CMS & Ecomm','CMS & Ecomm'),
        ('System Admin','System Admin'),
        ('UI/UX','UI/UX'),
        ('Quality Analyst','Quality Analyst'),
        ('HR','HR'),
    )
    department   = models.CharField(max_length=100, choices = DEPARTMENT_CHOICES)
    # timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employeename
    

    '''@property
    def owner(self):
        return self.user

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    
    def get_api_url(self, request=None):
        return api_reverse("postings:post-rud", kwargs={'pk': self.pk}, request=request)
'''