# users/models.py
#
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email


from django.db import models

# Create your models here.



class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
        

    LOAN_STATUS = (
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status= models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)   

    def __str__(self):
        """
        String for representing the Model object.
        """
        #return '%s (%s)' % (self.id,self.book.title)
        return '{0} ({1})'.format(self.id,self.book.title)
        

