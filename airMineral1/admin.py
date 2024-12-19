from django.contrib import admin
from .models import Pelanggan, JenisAirMineral, Produk, Transaksi, DetailTransaksi

# Registrasi model ke admin tanpa kustomisasi tambahan
admin.site.register(Pelanggan)
admin.site.register(JenisAirMineral)
admin.site.register(Produk)
admin.site.register(Transaksi)
admin.site.register(DetailTransaksi)
