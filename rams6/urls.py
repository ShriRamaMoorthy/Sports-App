"""rams6 URL Configuration

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
from django.urls import path, include
from product.views import base_view,contact_view,home_view,news_view, player_view,world_view,add_ply,remove_ply,filter_ply,table_view,aboutus_view,points_view

#OR ELSE
# from product.views import home_view

urlpatterns = [
    path('',base_view,name='home'),
    path('home/',home_view,name='home'),
    path('contactpage/',contact_view,name='contact page'),
    path('news/',news_view,name='news'),
    path('worldleague/',world_view,name='news'),
    path('admin/', admin.site.urls),
    path('players/',player_view, name='add_ply'),
    path('add_emp/',add_ply, name='add_ply'),
    path('remove_emp/', remove_ply, name='remove_ply'),
    path('remove_emp/<int:emp_id>', remove_ply, name='remove_ply'),
    path('filter_emp/',filter_ply, name='filter_ply'),
    path('view_all/',table_view, name='view all'),
    path('aboutus/',aboutus_view, name='view all'),
    path('pointstable/',points_view, name='view all'),
]



