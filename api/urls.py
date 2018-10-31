"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as view
from app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/$',views.tournamentform,name="tournament"),
    url(r'^login/$',views.loginpage,name="login"),
    url(r'^$',views.loginpage,name="login"),
    url(r'^dashboard/',views.dashboard,name="dashboard"),
    url(r'^transaction/',views.money,name="transaction"),
    url(r'^player/',views.player_details,name="player"),
    url(r'^money/',views.money_trans,name="money"),
    url(r'^winner/',views.winner,name="winner"),
    url(r'^position/',views.position,name="position"),
    url(r'^join/',views.playerjoin,name="join"),
    url(r'^status/',views.tournament,name="status"),
    url(r'^logout/$',view.logout,name= 'logout',kwargs={'next_page':'/login'}),
]
