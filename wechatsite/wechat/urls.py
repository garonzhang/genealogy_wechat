from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.wechat_interface,name='wechat_interface'),
]
