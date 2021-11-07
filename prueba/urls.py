"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .router import router
from .apps.apiUsers.views import MyTokenObtainPairView
from prueba.apps.apiUsers.api.viewsets import *

urlpatterns = [
    path(
        "admin/", 
        admin.site.urls
    ),
    path(
        "api/v1/users/login/", 
        MyTokenObtainPairView.as_view(), 
        name="token_obtain_pair"
    ),
    path(
        "api/v1/users/refresh/", 
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path(
        "api/v1/",
        include(router.urls)
    ),
]
