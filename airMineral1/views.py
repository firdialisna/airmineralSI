from django.shortcuts import render
from django.db.models import Sum
from .models import Transaksi, DetailTransaksi, Produk

def produk_stok_view(request):
    # Mengambil semua produk dan stok yang tersedia
    produk_stok = Produk.objects.all()

    # Mengirimkan data ke template
    return render(request, 'produk_stok.html', {'produk_stok': produk_stok})

def total_pendapatan_view(request):
    total_pendapatan = Transaksi.objects.filter(status='completed').aggregate(total=Sum('total_harga'))
    return render(request, 'total_pendapatan.html', {'total_pendapatan': total_pendapatan['total']})

def produk_terlaris_view(request):
    # Mengambil 5 produk terlaris berdasarkan jumlah transaksi yang terjual
    produk_terlaris = DetailTransaksi.objects.values('produk__nama') \
        .annotate(total_terjual=Sum('jumlah')) \
        .order_by('-total_terjual')[:5]
    
    # Mengirimkan data ke template
    return render(request, 'produk_terlaris.html', {'produk_terlaris': produk_terlaris})

def home(request):
    context = {}
    return render(request, "home.html", context)

def produk_view(request):
    # Mengambil semua data produk dari database
    produk_list = Produk.objects.all()

    # Mengirim produk_list ke template
    return render(request, 'produk.html', {'produk_list': produk_list})

