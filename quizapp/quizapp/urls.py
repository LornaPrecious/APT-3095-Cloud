"""
URL configuration for quizapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from users import views as v
from quiz import views as qv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  qv.landing, name ='landing'),
     path('home/',  qv.landing, name ='landing'),
    path('index/',  qv.index, name ='index'),
  
    
    path('register/', v.register, name ='register'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('login/', v.custom_login, name='login'), 
    path('logout/', v.signout, name='signout'), 
    path('activate/<uidb64>/<token>', v.activate, name='activate'),
    
]
