"""autopark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.users.views import UserViewSet, EmployeeViewSet, ProfileEdit
from accounts.companies.views import CompanyEditViewSet, CompanyView
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'profile_edit', ProfileEdit, basename='profile_edit')
router.register(r'company_view', CompanyView, basename='company_view')
# router.register(r'company_edit', CompanyEditViewSet, basename='company_edit')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('company_edit/', CompanyEditViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token-auth/', views.obtain_auth_token)
]
