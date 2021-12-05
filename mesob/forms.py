from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['first_name', 'last_name', 'email', 'number_of_guests', 'date_and_time' ]
