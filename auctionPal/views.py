from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def index(request):
    return render(request, "index.html", {})

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    print('User is logged in: ')
    print(request.user.is_authenticated())

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            context['form'] = LoginForm()
            
            return redirect('/login')
        else:
            # Return an 'invalid login' error message.
            print('Error')

    return render(request, 'auth/login.html', context)

