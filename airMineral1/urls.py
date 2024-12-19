from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path('produk_view/', views.produk_view, name='produk_view'),
    path('total_pendapatan/', views.total_pendapatan_view, name='total_pendapatan'),
    path('produk_stok/', views.produk_stok_view, name='produk_stok'),
    path('produk_terlaris/', views.produk_terlaris_view, name='produk_terlaris'),
]
