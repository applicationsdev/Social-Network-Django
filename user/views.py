# Imports
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# User Login view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        # Validation & authentication
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Your account is authenticated successfully')
                else:
                    return HttpResponse('Your account is currently disabled')
            else:
                return HttpResponse('Submitted login credentials are invalid')
                
    else:
        form = LoginForm()
    
    return render(request, 'user/login.html', {'form': form})
    
# User Dashboard view
@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html', {'section': 'dashboard'})
