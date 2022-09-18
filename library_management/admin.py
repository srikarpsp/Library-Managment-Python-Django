from django.contrib import admin


from .models import Book
from .models import BookType

class BookAdmin(admin.ModelAdmin):
	list_display = ('BookId', 'BookName', 'Author', 'Types', 'Publication', 'Published')
		
admin.site.register(Book, BookAdmin)
admin.site.register(BookType)