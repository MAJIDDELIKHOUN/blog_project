from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_app:home')
        else:
            return redirect('account_app:login')
    return render(request, 'account_app/login.html', {})


def logout_view(request):
    logout(request)
    return redirect('home_app:home')



def register_view(request):
    context={'errors':[]}
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password2!=password1:
            context['errors'].append('password are not same')
            return render(request,'account_app/register.html',context)
        elif User.objects.get(username=username):
            context['errors'].append('username exist')
            return render(request, 'account_app/register.html', context)
        user=User.objects.create(username=username,password=password1,email=email)
        login(request,user)
        return redirect('home_app:home')
    return render(request,'account_app/register.html')