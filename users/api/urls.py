from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (registration_view,update_view,active_officers,deactivate)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register',registration_view,name='api_register'),
    path('login',obtain_auth_token,name='api_login'),
    path('users',active_officers,name='active_officers'),
    path('users/deactivate/<int:id>',deactivate,name='api_deactivate'),
    path('update',update_view,name='api_update')
]

