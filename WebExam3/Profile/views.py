from django.shortcuts import render, redirect

from WebExam3.Book.models import Book
from WebExam3.Profile.forms import ProfileForm, DeleteProfileForm
from WebExam3.Profile.models import Profile


# Create your views here.
def home_page(request):
    profile = Profile.objects.first()
    books = Book.objects.all()

    rows = []
    per_row = 3

    for i in range(0, len(books), per_row):
        current_row = books[i: i + per_row]
        rows.append(current_row)

    form = ProfileForm()
    if not profile:
        form = ProfileForm()
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'home-with-profile.html', {'form': form, 'books': books, 'profile': profile, 'rows': rows})

        context = {
            'form': form,
            'profile': profile,
            'books': books,
            'rows': rows,
        }

        return render(request, 'home-no-profile.html', context)

    context = {
        'form': form,
        'profile': profile,
        'books': books,
        'rows': rows,
    }

    return render(request, 'home-with-profile.html', context)


def profile_page(request):
    profile = Profile.objects.get()

    form = ProfileForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    books = Book.objects.all()

    if request.method == "GET":
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            books.delete()
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-profile.html', context)
