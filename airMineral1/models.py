from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField  # Pastikan ini hanya digunakan jika dibutuhkan

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    alamat = models.TextField()
    telepon = models.CharField(max_length=15)

    def __str__(self):
        return self.nama

class JenisAirMineral(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Menambahkan slug
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()
    jenis_air_mineral = models.ForeignKey(JenisAirMineral, on_delete=models.CASCADE, related_name='produks')

    def save(self, *args, **kwargs):
        if not self.slug:  # Hanya buat slug jika belum ada
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama

class Transaksi(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE, related_name='transaksis')
    tanggal_transaksi = models.DateTimeField(auto_now_add=True)
    total_harga = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')])

    def __str__(self):
        return f"Transaksi {self.id} - {self.pelanggan.nama}"

class DetailTransaksi(models.Model):
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE, related_name='detail_transaksis')
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE, related_name='detail_transaksis')
    jumlah = models.IntegerField()
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        # Validasi jumlah
        if self.jumlah > self.produk.stok:
            raise ValueError("Jumlah melebihi stok yang tersedia.")
        
        # Update subtotal setiap kali detail transaksi disimpan
        self.subtotal = self.jumlah * self.produk.harga
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detail Transaksi {self.transaksi.id} - {self.produk.nama}"

    class Meta:
        verbose_name = "Detail Transaksi"
        verbose_name_plural = "Detail Transaksi"
