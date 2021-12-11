from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm

# Functions are adopted from course material and modified to fit project


def home(request):
    ''' Renders the home page'''
    return render(request, 'index.html')


def booking_view(request):
    ''' Renders the booking list page'''
    bookings = Book.objects.all().order_by(
        'date_and_time').filter(username=request.user)
    context = {
        'bookings': bookings
    }

    return render(request, 'booking_list.html', context)


def create_book(request):
    ''' Renders the booking page'''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            date_and_time = form.cleaned_data['date_and_time']
            # checks for double time booking
            if Book.objects.filter(date_and_time=date_and_time).exists():
                messages.success(request, 'Please book another time')
                return HttpResponseRedirect(reverse('book'))
            else:
                update = form.save(commit=False)
                update.username = request.user
                update.save()

        return redirect('booklist')
    form = BookForm()
    context = {
        'form': form
    }

    return render(request, 'book.html', context)


def update_book(request, book_id):
    ''' Renders the page for updating the booking'''

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


def cancel_book(request, book_id):
    ''' Function to cancel booking'''

    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('booklist')
