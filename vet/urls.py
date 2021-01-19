from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),

    # REST API Routes
    path('api/v1/account/', include('users.api.urls'))

] + staticfiles_urlpatterns()
