from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url, include
from rest_framework import routers
from food import views
from rest_framework_jwt.views import *
from django.conf.urls import url


router = routers.DefaultRouter()

router.register(r'tables', views.TableViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'service_percentage', views.ServiceViewSet)
router.register(r'meals', views.MealViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]