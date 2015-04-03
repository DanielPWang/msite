from django.contrib import admin
from .models import *

class AuthorInline(admin.TabularInline):
    model = Author
    extra = 1

class BooksInline(admin.TabularInline):
    model = Book
    extra = 1

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher")
    list_filter = ("title", "authors", "publisher")
    search_fields = ("title", "authors", "publisher")
    #inlines = ( AuthorInline, )

class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "website")
    list_filter = ("name", "country", "website")
    search_fields = ("name", "country", "website")
    inlines = ( BooksInline, )

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
