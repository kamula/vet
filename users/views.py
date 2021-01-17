from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import AccountAuthentication, userregistration
from django.contrib.auth.decorators import login_required
# registration view
def registration_view(request):
    context = {}
    if request.POST:
        form = userregistration(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email,password = raw_password)
            login(request,account)
            return redirect('login')
        else:
            context['registrationform'] = form
    else:
        form = userregistration()
        context['registrationform'] = form
    return render(request,'accounts/register.html',context)


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
                return redirect('dashboard')
    else:
        form = AccountAuthentication
    context['login_form'] = form
    return render(request, 'accounts/login.html')

# logout view
def logout_view(request):
    logout(request)
    return redirect('login')


# Dashboard
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
