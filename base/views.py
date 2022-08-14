from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Todo
from django.contrib.auth import authenticate, login, logout


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exits')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'base/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def signup(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {'form': form}
    return render(request, 'base/signup.html', context)


@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'base/todo.html', context)
