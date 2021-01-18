from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (registration_view)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register',registration_view,name='api_register'),
    path('login',obtain_auth_token,name='api_login')
]

