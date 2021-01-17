from django.urls import path,include
from .views import dashboard,login_view,logout_view

urlpatterns = [
    path('',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('dashboard/', dashboard, name = "dashboard")    
]
