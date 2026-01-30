from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    return HttpResponse("<h1>Login</h1>")


def register_view(request):
    return HttpResponse("<h1>Register</h1>")

def logout_view(request):
    return HttpResponse("<h1>Logout</h1>")