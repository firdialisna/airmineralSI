# Generated by Django 5.1.3 on 2024-12-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airMineral1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailtransaksi',
            options={'verbose_name': 'Detail Transaksi', 'verbose_name_plural': 'Detail Transaksi'},
        ),
        migrations.AddField(
            model_name='produk',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
