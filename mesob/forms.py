from django import forms
from .models import Book

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class BookForm(forms.ModelForm):
    date_and_time = forms.DateTimeField(widget=DateTimeInput, input_formats=["%Y-%m-%dT%H:%M", ])
    class Meta:
        model = Book
        fields = ['first_name', 'last_name', 'email', 'number_of_guests', 'date_and_time' ]


# check_in = DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])