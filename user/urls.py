# Imports
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

# User routes
urlpatterns = [
    # Public Profile
    url(r'^$', views.index, name='index'),
    
    # Login / logout
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    
    # Account Dashboard
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    
    # Register
    url(r'^register/$', views.register, name='register'),
]
