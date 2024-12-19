from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("airMineral1.urls")),  # Perbaiki tanda kurung dan tambahkan koma
]
