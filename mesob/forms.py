from django import forms
from .models import Book


class DateTimeInput(forms.DateTimeInput):
    ''' Datetime picking widget '''
    input_type = 'datetime-local'


class BookForm(forms.ModelForm):
    '''Booking form which also specifies
    date and time format '''
    date_and_time = forms.DateTimeField(widget=DateTimeInput,
                                        input_formats=["%Y-%m-%dT%H:%M", ])

    class Meta:
        '''Specifiying model fields'''
        model = Book
        #fields = ['first_name', 'last_name', 'email', 'number_of_guests',
        #         'date_and_time']
        exclude = ['username']

