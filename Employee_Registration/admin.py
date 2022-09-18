from django.contrib import admin


from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('Employeeid', 'employeename', 'contact', 'email', 'department')

admin.site.register(Employee, EmployeeAdmin)