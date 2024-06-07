from django.shortcuts import redirect, render
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def user_register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created, you can log in')
            return redirect('login')
    else:
        form=RegisterForm()

    return render(request,'register.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('/')
