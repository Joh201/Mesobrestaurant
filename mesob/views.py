from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.

def home(request):
    return render(request, 'index.html')


def booking_view(request):
    bookings = Book.objects.all().order_by('date_and_time')
    context = {
        'bookings': bookings
    }
    return render(request, 'booking_list.html', context)


def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('booklist')
    form = BookForm()
    context = {
        'form': form
    }

    return render(request, 'book.html', context)


def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('booklist')
    form = BookForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'updatebook.html', context)




