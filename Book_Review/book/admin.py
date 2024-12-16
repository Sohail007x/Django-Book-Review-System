from django.contrib import admin
from book.models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','description','genre','isbn','publish_date','average_rating')