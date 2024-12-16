from django.urls import path
from book.views import create_book,book_list,book_detail,book_update,book_delete

urlpatterns = [
    path('new/',create_book,name='create-book'),
    path('booklist/',book_list,name='book-list'),
    path('detail/<int:id>/',book_detail,name='book-detail'),
    path('update/<int:id>/',book_update,name='book-update'),
    path('delete/<int:id>/',book_delete,name='book-delete')
]