# Imports
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

# User routes
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]
