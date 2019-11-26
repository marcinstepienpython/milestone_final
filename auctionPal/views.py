from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect



def index(request):
    
    return render(request, "index.html", {})
