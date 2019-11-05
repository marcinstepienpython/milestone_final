from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm

def index(request):
    return render(request, "index.html", {})

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            context['form'] = LoginForm()
            
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            print('Error')

    return render(request, 'auth/login.html', context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        new_user = User.objects.create_user(username, email, password)
        return redirect('/login')


    return render(request, 'auth/register.html', context)