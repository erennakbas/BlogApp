from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def login_request(request):
    if (request.method=="POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            login(request,user)
            return redirect("home")
        else: 
            return render(request, "account/login.html",{
                "error": "Incorrect credentials. Try again."
            })
    return render(request, "account/login.html")
# Create your views here.
def register_request(request):
    if (request.method=="POST"):
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if (password==confirm_password):
            if (User.objects.filter(username=username).exists()):
                return render(request, "account/register.html",{
                "error": "Username is already taken"
            })
            elif (User.objects.filter(email=email).exists()):
                return render(request, "account/register.html",{
                "error": "Email is registered. Did you forget your password?"
            })
            else:
                user = User.objects.create_user(email=email, username=username, password=password )
                user.save()
                authenticated_user=authenticate(username=username, password=password)
                login(request,authenticated_user)
                return redirect("home")
        else: 
            return render(request, "account/register.html",{
                "error": "Password mismatch"
            })
    return render(request, "account/register.html")
def logout_request(request):
    logout(request)
    return redirect("home")
