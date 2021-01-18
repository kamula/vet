from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (registration_view)

urlpatterns = [
    path('register',registration_view,name='api_register')
]

