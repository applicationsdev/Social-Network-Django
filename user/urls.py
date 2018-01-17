# Imports
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

# Urls
urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]