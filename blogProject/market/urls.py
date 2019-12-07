from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.market, name="market"),
    path('<int:market_id>', views.detail, name="detail"),
    path('<int:market_id>/order', views.order, name="order"),
    path('new', views.new, name="new"),
    path('market_serach', views.market_search, name="market_search"),
    path('create', views.create, name="create"),
    path('delete/<int:market_id>',views.delete, name="delete"),
    path('menu/create/<int:market_id>', views.menu_create,name="menu_create"),
    path('like/<int:market_id>',views.post_like, name="post_like"), # 즐겨찾기 위한 url
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
