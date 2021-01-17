from django.urls import path,include
from .views import dashboard,login_view,registration_view,logout_view,add_user,users_view

urlpatterns = [
    path('',login_view,name='login'),
    path('register/',registration_view,name='register'),
    path('adduser/',add_user,name='adduser'),
    path('users/',users_view,name='users'),
    path('logout/',logout_view,name='logout'),
    path('dashboard/', dashboard, name = "dashboard")    
]
