# Imports
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# User - Public Profile page view
def index(request):
    return render(request, 'pages/index.html', {'section': 'index'})

# User - Login view
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
    
# User - Account Dashboard view
@login_required
def dashboard(request):
    return render(request, 'private/dashboard.html', {'section': 'dashboard'})

# User - Registration view
def register(request):
    if request.method == 'POST':
        registerForm = UserRegistrationForm(request.POST)
        
        if registerForm.is_valid():
            newUser = registerForm.save(commit=False)
            newUser.set_password(registerForm.cleaned_data['password'])
            newUser.save()
            
            login(request, newUser)
            HttpResponse('Your new account has been created successfully')
            return redirect('/user/dashboard/')
            
    else:
        registerForm = UserRegistrationForm()
    
    return render(request, 'registrationCustom/register.html', {'registerForm': registerForm})
