from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'You have logged in successfully.')
                    return redirect('dashboard')  # Redirect to dashboard after login
                else:
                    messages.error(request, 'Your account is disabled.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
