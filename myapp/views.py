# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
# myapp/views.py

def home_redirect(request):
    return redirect('login')  # Редирект на URL с именем 'login'


def register_view(request):
    print("Register view called")  # отладочный вывод
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.username = form.cleaned_data['email']
            user.save()
            login(request, user)
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})

def login_view(request):
    print("Login view called")  # отладочный вывод
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('success')
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})

@login_required
def success_view(request):
    print("Success view called")  # отладочный вывод
    return render(request, 'myapp/success.html')
