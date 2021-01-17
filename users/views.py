from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import AccountAuthentication, userregistration
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .counties import counties
from .models import Users
# registration view


def registration_view(request):
    context = {
        "counties": counties
    }
    if request.POST:
        form = userregistration(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_password)
            return redirect('login')
        else:
            context['registrationform'] = form
    else:
        form = userregistration()
        context['registrationform'] = form
    return render(request, 'accounts/register.html', context)

# Add user view


@login_required(login_url='login')
def add_user(request):
    context = {
        "counties": counties
    }
    if request.POST:
        form = userregistration(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_password)
            return redirect('users')
        else:
            context['registrationform'] = form
    else:
        form = userregistration()
        context['registrationform'] = form
    return render(request, 'accounts/adduser.html', context)


# login view
def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        # redirect to dashboard if user is valid
        return redirect('dashboard')
    if request.method == 'POST':
        form = AccountAuthentication(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                # redirect to dashboard if user is
                return redirect('users')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')
    else:
        form = AccountAuthentication()
    context['login_form'] = form
    return render(request, 'accounts/login.html')

# logout view


def logout_view(request):
    logout(request)
    return redirect('login')

# users
# redirect to login page if user is not logged in
@login_required(login_url='login')
def users_view(request):
    users = Users.objects.order_by("-date_joined").exclude(is_superuser=True)
    context = {
        "users": users
    }
    return render(request, "accounts/users.html", context)

# Dashboard


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
