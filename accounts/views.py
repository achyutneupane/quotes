from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, first_name= firstname, last_name= lastname, email=email, password=password1)
                user.save();

                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
        else:
            print("Password not matched ")
    else:
        return render(request,'pages/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Wrong username and password")
            return redirect('signin')
    else:
        return render(request,'pages/signin.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


