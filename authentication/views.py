from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    # return HttpResponse("<h1>Register</h1>")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    
    else:
        initail_data = {'username' : '', 'password1' : '', 'password2' : ""}
        form = UserCreationForm(initial = initail_data)
        
    return render(request, 'auth/register.html', {'form' :form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        
    else:
        initial_data = {'username' : "", "password" : ""}
        form = AuthenticationForm(initial = initial_data)
        
    return render(request, 'auth/login.html', {'form' : form})

def logout_view(request):
    logout(request)
    return render(request,'auth/login.html')