from django.contrib import admin
from django import forms

from .models import Assignbook, Bookdetails

class AssignbookForm(forms.ModelForm):
    # some normal ModelForm setup goes here
    def clean(self):
        cleaned_data = super(AssignbookForm, self).clean()
        issue = cleaned_data.get("issue")
        renew = cleaned_data.get("renew")

        if issue and renew:
            if renew < issue:
                raise forms.ValidationError("renew time cannot be earlier than issue time!")
        return cleaned_data

class AssignAdmin(admin.ModelAdmin):
	list_display = ('Employeeid', 'BookId', 'issue', 'renew')

admin.site.register(Assignbook, AssignAdmin)

class BookdetailsAdmin(admin.ModelAdmin):
     list_display = ('Employeeid',)

admin.site.register(Bookdetails, BookdetailsAdmin)