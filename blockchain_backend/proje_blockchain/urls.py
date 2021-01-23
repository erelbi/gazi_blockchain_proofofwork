"""proje_blockchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers
from django.urls import path,include
from proje_blockchain.node1.views import CreatBlock,Mining,BlockView,run_miner
router = routers.DefaultRouter()
router.register('view', BlockView, basename='view')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('create/', CreatBlock.as_view(), name="create"),
    path('mining/', Mining.as_view(), name="mining"),
    path('miner/', run_miner, name="miner"),
]
