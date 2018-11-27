from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url, include
from rest_framework import routers
from food import views
from rest_framework_jwt.views import *
from django.conf.urls import url

router = routers.DefaultRouter()

router.register(r'login', views.LoginView)
router.register(r'registration', views.RegistrationView)


urlpatterns = [
    url(r'^', include(router.urls)),
]