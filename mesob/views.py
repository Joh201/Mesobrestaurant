from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    return render(request, 'index.html')


def booking_view(request):
    bookings = Book.objects.all().order_by('date_and_time')
    context = {
        'bookings': bookings
    }
    return render(request, 'booking_list.html', context)




