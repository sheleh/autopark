from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.companies.urls')),
    path('api/', include('accounts.users.urls')),
    path('api/', include('offices.urls')),
    path('api/', include('vehicles.urls')),
    # Authorization
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token-auth/', views.obtain_auth_token)
]
