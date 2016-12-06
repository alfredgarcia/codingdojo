#CONTROLLER in django, create your views here:
from django.shortcuts import render

def index(request):
    response = "Hello, I am your first request!"
    return render(request, "first_app/index.html")
