from rest_framework import routers
from django.urls import path, include
from .views import CompanyEditView, CompanyView

router = routers.DefaultRouter()
router.register(r'company_view', CompanyView, basename='company_view')

urlpatterns = [
    path('', include(router.urls)),
    path('company_edit/', CompanyEditView.as_view())
]