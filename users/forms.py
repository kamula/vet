from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Users

# user registration


class userregistration(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Users
        fields = ('name','email', 'county', 'id_no', 'phone_number')
# user account authentication


class AccountAuthentication(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login credentials')
