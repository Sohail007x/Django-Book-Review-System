from django.shortcuts import render,redirect
from book.forms import BookForm
from book.models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Book Created Successfully")
            return redirect('create-book')
        else:
            messages.error(request,"There was an Error while creating a book")
    else:
        form = BookForm()
    return render(request,'book/book_form.html',{'form':form})

@login_required(login_url='login')
def book_list(request):
    books = Book.objects.all().order_by('-created_at') #Order by date carrying from models
    return render(request, 'book/book_list.html',{'book':books})

@login_required(login_url='login')
def book_detail(request,id):
    book = Book.objects.get(id=id)
    return render(request,'book/book_detail.html',{'book':book})

@login_required(login_url='login')
def book_update(request,id):
    book = Book.objects.get(id=id)
    
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            messages.success(request,"Book Updated Successfully")
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
    return render(request,'book/book_update.html',{'form':form})

@login_required(login_url='login')
def book_delete(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request,"Book Deleted Successfully")
    return redirect('book-list')