from django.urls import path

from WebExam3.Book.views import book_add, book_edit, book_details, book_delete

urlpatterns = (
    path('add/', book_add, name='book-add'),
    path('edit/<int:id>/', book_edit, name='book-edit'),
    path('details/<int:id>/', book_details, name='book-details'),
    path('book/delete/<int:id>/', book_delete, name='book-delete'),
)