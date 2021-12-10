from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ''' Class that facilitates the management of the admin panel '''
    # list_displaly = ('last_name', 'email', 'number_of_guests')
    list_filter = ('first_name', 'date_and_time')
    search_fields = ['first_name', 'number_of_guests']
