from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import LoginForm

def index(request):
    return render(request, 'loginapp/index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid login details')
    return render(request, 'loginapp/login.html', {'form': LoginForm})

def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out!!')
    return redirect('/')

