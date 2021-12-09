from django.contrib import admin
from .models import Book

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # list_displaly = ('first_name', 'email', 'number_of_guests',
    #                  'date_and_time')
    list_filter = ('first_name', 'date_and_time')
    search_fields = ['first_name', 'date_and_time', 'number_of_guests']

