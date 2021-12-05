from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_displaly = ('first_name', 'last_name','number_of_guests', 'date_and_time', 'email')


