from rest_framework import serializers

from Book_Management.models import Assignbook, Bookdetails
from library_management.models import Book
from Employee_Registration.models import Employee

class AssignbookSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Assignbook
        fields = ('id', 'url', 'Employeeid', 'BookId', 'issue', 'renew')
        
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'url', 'BookId')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'url', 'Employeeid')

class BookdetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee 
        fields = ('id', 'url', 'Employeeid', 'assignbook')    
    


        #'timestamp','url',
        # read_only_fields = ['id', 'user']
'''
    # converts to JSON
    # validations for data passed

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_postings_url(request=request)

    def validate_title(self, value):
        qs = EmployeePost.objects.filter(title__iexact=value) # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value
'''