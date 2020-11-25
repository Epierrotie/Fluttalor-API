"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from api.view import UserCreate
from contact.view import ContactApi
from label.view import LabelApi

from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/contact', ContactApi, 'contact')
router.register('api/label', LabelApi, 'label')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/user/register/', UserCreate.as_view({'post': 'create'}), name='register'),
    path('api/user/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/user/', include('rest_framework.urls', namespace='logout')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

] + router.urls
