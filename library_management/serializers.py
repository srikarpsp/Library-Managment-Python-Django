from rest_framework import serializers

from library_management.models import Book,BookType


class BookSerializer(serializers.HyperlinkedModelSerializer): # forms.ModelForm
    #url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Book
        fields = ('id', 'url', 'BookId', 'Types', 'BookName', 'Author', 'Publication', 'Published')
    
class BookTypeSerializer(serializers.HyperlinkedModelSerializer): # forms.ModelForm
    #url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BookType
        fields = ('id', 'url', 'Types')



        #'timestamp','url',
        # read_only_fields = ['id', 'user']
'''   
    # converts to JSON
    # validations for data passed

    def get_url(self, obj):
         #request
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