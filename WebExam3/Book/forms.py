from django import forms

from WebExam3.Book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'title': forms.TextInput({'placeholder': 'Title'}),
            'description': forms.Textarea({'placeholder': 'Description'}),
            'image': forms.URLInput({'placeholder': 'Image'}),
            'type': forms.TextInput({'placeholder': 'Fiction, Novel, Crime...'}),
        }
