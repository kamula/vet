from django.urls import path, include
from .views import dashboard, login_view, registration_view, logout_view, add_user, users_view, deactivate, edit_user, user_update

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('adduser/', add_user, name='adduser'),
    path('users/', users_view, name='users'),
    path('users/<int:id>', edit_user, name='edit_user'),
    path('update/', user_update, name='update_user'),
    path('users/<str:email>', deactivate, name='deactivate'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name="dashboard")
]
