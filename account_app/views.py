from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm,RegisterForm


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home_app:home')

    else:
        form = LoginForm()
    return render(request, 'account_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home_app:home')


def register_view(request):
    # context={'errors':[]}
    form = RegisterForm(data=request.POST)
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            # if password2!=password1:
            #   context['errors'].append('password are not same')
            #    return render(request,'account_app/register.html',context)
            # elif User.objects.get(username=username):
            #    context['errors'].append('username exist')
            #    return render(request, 'account_app/register.html', context)
            user = User.objects.create(username=username, password=password1, email=email)
            login(request, user)
            return redirect('home_app:home')
        else:
            return render(request, 'account_app/register.html', {'form': form})
    return render(request, 'account_app/register.html', {'form': form})
