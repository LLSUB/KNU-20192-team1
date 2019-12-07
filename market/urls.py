from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('',views.market, name="market"),
    path('<int:market_id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create, name="create"),
    path('menu/create/<int:market_id>', views.menu_create,name="menu_create"),
    path('like/<int:market_id>',views.post_like, name="post_like"), # like를 위한 url
]
