from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('podcast:list')
    ctx = {
        'form': form
    }
    return render(request, 'login.html', ctx)


def logout_view(request):
    if not request.user.is_anonymous:
        if request.method == 'POST':
            logout(request)
            return redirect('podcast:index')
    else:
        return redirect('logout.html')

    return render(request, 'logout.html')


def register_view(request):
    if not request.user.is_anonymous:
        return redirect('podcast:list')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('podcast:list')
    ctx = {
        'form':form
    }
    return render(request, 'register.html', ctx)