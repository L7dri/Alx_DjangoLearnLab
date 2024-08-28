from django.contrib import admin

from .models import Book
admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')
    
    # Add filters for the list view
    list_filter = ('author', 'publication_year')
