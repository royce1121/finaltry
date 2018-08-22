from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^account/$', views.check, name='check'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^create/$', views.create, name='create'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
]