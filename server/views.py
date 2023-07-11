from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import RegisterUserForm, LoginForm, PasswordResetForm, ChangePasswordForm
from fileApp.models import File
from mailer import send_email
from django.contrib.sites.shortcuts import get_current_site
import hashlib


# Create your views here.

def login(request):

    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            is_activated = User.objects.get(username=username)

            if is_activated.is_active != True:
                messages.info(request, "Please go to your mail and click on the link to activate your account.")
                return redirect("/login")

            auth.login(request, user)
            return redirect("/dashboard")
               
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
        user.is_active = False
        user.save()

        user_to_activate = User.objects.get(email=email)
        hash = hashlib.sha256()
        hash.update(f"{user_to_activate.username}{user_to_activate.last_name}{user_to_activate.date_joined}".encode('utf-8'))
        link = f"{get_current_site(request).domain}/activate/{user_to_activate.username}/{hash.hexdigest()}"
        send_email(to=email, 
                       body=f"Click  on the link to activate your account. Link: {link}",
                       subject="Activate your account.")


        messages.success(request, "Sign Up sucessful.")
        return redirect('login')
    
    
    return render(request, "signup.html", {"form": RegisterUserForm()})

def logout(request):
    auth.logout(request)
    messages.info(request, "Successfully Logged Out")
    return redirect("/login")

def dashboard(request):
    files = File.objects.all()
    return render(request, "dashboard.html", {"files": files})

def home(request):
    return redirect("/dashboard")

def webroot(request):
    return redirect("/login")

def password_reset(request):
    if request.POST:
        email = request.POST["email"]
        user = User.objects.filter(email=email)

        if user.exists():
            user = User.objects.get(email=email)
            hash = hashlib.sha256()
            hash.update(f"{user.first_name}{user.last_name}{user.date_joined}".encode('utf-8'))
            link = f"{get_current_site(request).domain}/token/{user.username}/{hash.hexdigest()}"
            send_email(to=email, 
                       body=f"Click  on the link to reset your password. Link: {link}",
                       subject="Reset your password.")
            print("[+] Sent ")
            messages.info(request, f"Check {email} for password reset link.")

    return render(request, "password_reset.html", {"form": PasswordResetForm()})

def password_reset_confirm(request, token, user):
    if request.POST:
        user_object = User.objects.get(username=user)
        
        if user_object:
            hash = hashlib.sha256()
            hash.update(f"{user_object.first_name}{user_object.last_name}{user_object.date_joined}".encode('utf-8'))
            orginal_token = hash.hexdigest()

            if token == orginal_token:
                password = request.POST["password1"]
                user_object.set_password(password)
                user_object.save()
                messages.success(request, "Password Changed Successfully.")
                return render(request, "password_reset_form.html", {"form": ChangePasswordForm()})

            
            messages.info(request, "Inavlid Password Reset Token.")

    return render(request, "password_reset_form.html", {"form": ChangePasswordForm()})


def activate_account(request, token, user):
    user_obj = User.objects.get(username = user)

    if user_obj:
        hash = hashlib.sha256()
        hash.update(f"{user_obj.username}{user_obj.last_name}{user_obj.date_joined}".encode('utf-8'))
        orginal_token = hash.hexdigest()

        if token == orginal_token:
            user_obj.is_active = True
            user_obj.save()
            messages.success(request, "Account Activated.")
            return render(request, "account_activated.html")

        messages.info(request, "Inavlid Account activation Reset Token.")
    return redirect("/login")