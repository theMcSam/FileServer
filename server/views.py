from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import RegisterUserForm, LoginForm, PasswordResetForm
from fileApp.models import File
from mailer import send_email

# Create your views here.

def login(request):

    if  request.POST:
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/dashboard")
        else:    
            messages.info(request, "Wrong username or password.")

    return render(request, "login.html", {"form":LoginForm()})
    

def signup(request):    
    if request.POST:
        uname = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        fname = request.POST["first_name"]
        lname = request.POST["last_name"]
        
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
    
    
    return render(request, "signup.html", {"form": RegisterUserForm()})

def logout(request):
    auth.logout(request)
    messages.info("Successfully Logged Out")
    return redirect("/login")

def dashboard(request):
    files = File.objects.all()
    return render(request, "dashboard.html", {"files": files})

def home(request):
    return redirect("dashboard")

def password_reset(request):
    if request.POST:
        email = request.POST["email"]

        if User.objects.filter(email=email).exists():
            send_email(to=email, body="")
            messages.info(request, f"Check {email} for password reset link.")

    return render(request, "password_reset.html", {"form": PasswordResetForm()})