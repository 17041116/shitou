#encoding:utf-8
from django.conf.urls import url
from . import views
app_name='user'
urlpatterns=[
    url(r'^$',views.require_login,name='require_login'),
    url(r'^login/$',views.require_login,name='require_login'),
]
