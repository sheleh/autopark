from django.urls import path, include
from . views import ProfileEdit, CreateSuperUser, EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')

urlpatterns = [
    # Provide current user profile view and edit
    path('', include(router.urls)),
    path('profile_edit/', ProfileEdit.as_view()),
    path('create_company_admin/', CreateSuperUser.as_view(), name='create_company_admin'),
]
