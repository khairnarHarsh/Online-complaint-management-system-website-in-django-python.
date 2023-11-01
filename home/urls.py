"""complaintsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from home import views
# from rest_framework import authtoken
# from rest_framework.authtoken import views
# from rest_framework_simplejwt.views import(
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('login1/', views.login1, name='login1'),
    path('studentlog/', views.studentlog, name='studentlog'),
    path('adminlog/', views.adminlog, name='adminlogin'),
    path('regist/', views.regist, name='regist'),
    path('profile/', views.profile, name='profile'),
    path('addcom/', views.addcom, name='addcom'),
    path('allcom/', views.allcom, name='allcom'),
    path('solvedcom/', views.solvedcom, name='solvedcom'),
    path('unsolvedcom/', views.unsolvedcom, name='unsolvedcom'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
    path('admin_dash/', views.admin_dash, name='admin_dash'),
    path('mycom/', views.mycom, name='mycom'),
    path('logout', views.logoutuser , name='logout'),
    path('editpage/', views.editpage, name='editpage'),
    path('pdf_report_create/<int:pid>/', views.pdf_report_create, name="pdf_report_create"),
    path('delete/<int:pid>/', views.delete, name="delete"),
    
]
