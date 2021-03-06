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
from django.conf.urls import url

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from api.views import UserApi
from contact.views import ContactApi
from label.views import LabelApi

from rest_framework import routers

router = routers.DefaultRouter()
router.register('contact', ContactApi, 'contact')
router.register('label', LabelApi, 'label')
router.register('user', UserApi, 'user')

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Fluttalor API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', schema_view)
] + router.urls
