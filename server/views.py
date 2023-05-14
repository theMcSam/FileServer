from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def login(request):

    if  request.POST:
        username = request.POST["uname"]
        password = request.POST["passwd"]

        if username == 'McSam' and password == 'password':
            return JsonResponse({'logged in successfully.'})
        
    return render(request, "login.html")
    
    # return JsonResponse({'Wrong username or password.'})
    

def signup(request):
    return JsonResponse({'msg':'Working properly'})
    ...