from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import AccountAuthentication, userregistration
# registration view
# def registration_view(request):
#     return


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



# Dashboard
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
