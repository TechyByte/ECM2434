"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from capturecampus import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.landing_page_request, name="landingpage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("home/<str:username>/", views.home, name="home"),
    path("teamcreation/", views.teamcreate_request, name="teamcreation"),
    path("capture_flag/", views.capture_flag, name="capture_flag"),
    path("add_flag/", views.flagcreate_request, name="create_flag"),
    path("QUEENS/", views.queens, name="Queens"),
    path("INTO/", views.into, name="Into"),
    path("SPORT/", views.sport, name="sport"),
    path("AMOURY/", views.amoury, name="amoury"),
    path("EAST/", views.east, name="East"),
    path("BUISNESS/", views.buisness, name="buisness"),
    path("ROWE/", views.rowe, name="rowe"),
    path("WASHINGTON/", views.washington, name="washington"),
    path("FORUM/", views.forum, name="forum"),
    path("playercreation/", views.playercreate_request, name="playercreation")

]
urlpatterns += staticfiles_urlpatterns()