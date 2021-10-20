from rest_framework import routers
from django.urls import path, include
from . views import AdminOfficesViewSet, ViewOffice

router = routers.DefaultRouter()
router.register(r'offices', AdminOfficesViewSet, basename='offices')
router.register('office_view', ViewOffice, basename='office_view')

urlpatterns = [
    path('', include(router.urls)),
]
