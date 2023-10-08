from django.shortcuts import render, redirect

from WebExam3.Book.forms import BookForm
from WebExam3.Book.models import Book
from WebExam3.Profile.models import Profile


# Create your views here.
def book_add(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        form = BookForm()
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'add-book.html', context)


def book_edit(request, id):
    book = Book.objects.filter(pk=id).get()
    profile = Profile.objects.first()

    if request.method == "GET":
        form = BookForm(instance=book)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'book': book,
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit-book.html', context)


def book_delete(request, id):
    book = Book.objects.filter(pk=id).get()
    book.delete()

    return redirect('index')


def book_details(request, id):
    book = Book.objects.filter(pk=id).get()
    profile = Profile.objects.first()

    context = {
        'book': book,
        'profile': profile,
    }

    return render(request, 'book-details.html', context)
