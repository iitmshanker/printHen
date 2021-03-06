"""printhen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/',views.admin,name='admin'),
    url(r'^api/setmailconfig/',views.setMailConfig,name='setMailConfig'),
    url(r'^api/getprinthistory/',views.getPrintHistory,name='getPrintHistory'),
    url(r'^credentialserror', TemplateView.as_view(template_name='printhen/credentialserror.html')),
]
