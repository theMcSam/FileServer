from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):

    if  request.POST:
        username = request.POST["uname"]
        password = request.POST["passwd"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, "dashboard.html", {"name":username})
        
    return render(request, "login.html")
    

def signup(request):    
    if request.POST:
        uname = request.POST["uname"]
        email = request.POST["email"]
        password1 = request.POST["passwd1"]
        password2 = request.POST["passwd2"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        
        if password1 != password2:
            messages.info(request, "Passwords do not match!")
            return redirect("signup")
        
        if User.objects.filter(username=uname).exists():
            messages.info(request, "User name already taken!")
            return redirect("signup")
        
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email has already been used!")
            return redirect("signup")
        
        user = User.objects.create_user(
            username = uname,
            password = password1,
            email = email,
            first_name = fname,
            last_name = lname
        )
        user.save()

        return redirect('login')
    
    
    return render(request, "signup.html")

def logout(request):
    auth.logout(request)
    return redirect("/")
