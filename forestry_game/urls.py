"""forestry_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from forestry_game import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RegisterView, LoginView, LevelView, LevelUpdateView, ReportView
from django.contrib.auth.models import User
from forestry_game.serializers import LevelSerializer, ReportSerializer, RegisterSerializer, LoginSerializer

urlpatterns = [
	#Admin urls
    url(r'^admin/', admin.site.urls),
    #Main urls
    url(r'^$', views.home ),
    #Authentication
    #url(r'^register/', views.register),
    #Api urls
    url(r'^api/v1/auth/register', RegisterView.as_view(queryset = User.objects.all(), serializer_class = RegisterSerializer), name="register" ),
    url(r'^api/v1/auth/login', LoginView.as_view(), name="login" ),
    url(r'^api/v1/auth/logout', views.logoutView, name="logout" ),
    url(r'^api/v1/level/$', LevelView.as_view(), name="level" ),
    url(r'^api/v1/level/update', LevelUpdateView.as_view(), name="levelupdate" ),
    url(r'^api/v1/level/delete', LevelView.as_view(), name="leveldelete" ),
    url(r'^api/v1/report/', ReportView.as_view(), name="report" ),
    url(r'^api/v1/validate/', views.validate),
    #Image url
    url(r'^levelimage/(?P<id>\d+).svg$', views.levelImageView, name="levelimage" ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
