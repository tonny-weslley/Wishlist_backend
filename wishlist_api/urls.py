from django.urls import path, include, re_path
from rest_framework import routers

from . import views, admin
from .views import UsuarioViewSet, WishViewSet, ListViewSet, AuthViewSet

app_name = 'wishlist_api'
router = routers.DefaultRouter()
router.register(r'users', UsuarioViewSet)
router.register(r'wish', WishViewSet)
router.register(r'list', ListViewSet)
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]