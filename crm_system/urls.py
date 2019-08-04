"""crm_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.views import *
from django.conf.urls import url
from crm_system.crm_food import views

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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
