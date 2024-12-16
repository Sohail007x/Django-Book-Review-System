from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth .decorators import login_required

# Create your views here.

#@login_required(login_url='login')

def signup(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Password didn't matched")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passwd = request.POST.get('pass')
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            auth_login(request,user)
            return redirect ('book-list')
        else:
            return HttpResponse("Invalid Credentials")
        
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect ('login')
