from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('api/external-news/', views.external_news, name='external_news'),
    path('api/internal-news/', views.internal_news, name='internal_news'),
]
