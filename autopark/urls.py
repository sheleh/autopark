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
from accounts.users.views import CreateSuperUser, EmployeeViewSet, ProfileEdit
from accounts.companies.views import CompanyEditView, CompanyView
from offices.views import OfficesView, ViewOffice
from vehicles.views import VehicleViewSet, ViewListVehicle
from rest_framework.authtoken import views

router = routers.DefaultRouter()

router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'company_view', CompanyView, basename='company_view')
router.register(r'offices', OfficesView, basename='offices')
router.register('office_view', ViewOffice, basename='office_view')
router.register('vehicle_create_edit', VehicleViewSet, basename='vehicle_create_edit')
router.register(r'vehicles_view', ViewListVehicle, basename='vehicles_view')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('create_company_admin/', CreateSuperUser.as_view(), name='create_company_admin'),
    path('company_edit/', CompanyEditView.as_view()),
    path('profile_edit/', ProfileEdit.as_view()),
    # Authorization
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token-auth/', views.obtain_auth_token)
]
