"""wechatsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from wechat.views import search_by_keyword, search_by_id 

urlpatterns = [
    url('wx', include('wechat.urls')),  # 增加此行
    url('s_name', search_by_keyword),  # 增加此行
    url('s_id', search_by_id),  # 增加此行
    path('admin/', admin.site.urls),
]
