from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
# from .forms import LoginForm, RegisterForm


def index(request):
    # print(request.session.get('first_name', 'unknown'))
    return render(request, "index.html", {})
