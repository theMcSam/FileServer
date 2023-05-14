from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def login(request):

    if  request.POST:
        username = request.POST["uname"]
        password = request.POST["passwd"]


        if username == 'mcsam' and password == 'password':
            print("Done")
            return JsonResponse({'msg':'logged in successfully.'})
        
    return render(request, "login.html")
    

def signup(request):
    username = request.POST["uname"]
    email = request.POST["email"]
    password = request.POST["passwd"]
    
    if request.POST:
        ...

    return render(request, "signup.html")