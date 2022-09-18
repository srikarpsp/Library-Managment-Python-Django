# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model as user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
User = user_model()
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name']

admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin

# Register your models here.

from .models import  BookInstance

"""
# Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""









@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """
    Administration object for BookInstance models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('book', 'status', 'borrower','due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )