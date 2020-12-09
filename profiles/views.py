from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .models import User
from .form import SignUpForm
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.forms import AuthenticationForm
import json


# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

def check_user_exists(request):
    uname = request.GET.get('uname')
    check = User.objects.filter(username__iexact=uname).exists()
    exists = {
        'status': check
    }
    return JsonResponse(exists, safe=False)

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.is_superuser:
                return redirect('index')

            elif request.user.user_type == 'dealer':
                return redirect('dashboard')
            else:
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})
