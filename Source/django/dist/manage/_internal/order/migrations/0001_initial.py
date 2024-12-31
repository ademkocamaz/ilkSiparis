# Generated by Django 5.1.4 on 2024-12-31 08:58

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('current', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLineCurrency',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('name', models.CharField(max_length=500, verbose_name='Adı')),
                ('symbol', models.CharField(max_length=500, verbose_name='Sembol')),
            ],
            options={
                'verbose_name': 'Para Birimi',
                'verbose_name_plural': 'Para Birimleri',
            },
            bases=('core.base',),
        ),
        migrations.CreateModel(
            name='OrderState',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('name', models.CharField(max_length=500, verbose_name='Adı')),
            ],
            options={
                'verbose_name': 'Sipariş Durumu',
                'verbose_name_plural': 'Sipariş Durumları',
            },
            bases=('core.base',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('date', models.DateTimeField(default=datetime.datetime(2024, 12, 31, 11, 58, 5, 464226), verbose_name='Tarih')),
                ('shipment_date', models.DateTimeField(blank=True, null=True, verbose_name='Sevk Tarihi')),
                ('invoice_number', models.CharField(blank=True, max_length=500, null=True, verbose_name='Fatura No')),
                ('number', models.CharField(blank=True, max_length=500, null=True, verbose_name='Sipariş No')),
                ('order_current', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_current', to='current.current', verbose_name='Cari')),
                ('order_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_state', to='order.orderstate', verbose_name='Sipariş Durumu')),
            ],
            options={
                'verbose_name': 'Sipariş',
                'verbose_name_plural': 'Siparişler',
            },
            bases=('core.base',),
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('quantity', models.DecimalField(decimal_places=5, max_digits=20, verbose_name='Miktar')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=20, null=True, verbose_name='Birim Fiyat')),
                ('total_price', models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=20, null=True, verbose_name='Toplam Fiyat')),
                ('city', models.CharField(blank=True, max_length=500, null=True, verbose_name='Şehir')),
                ('country', models.CharField(blank=True, max_length=500, null=True, verbose_name='Ülke')),
                ('related_person', models.CharField(blank=True, max_length=500, null=True, verbose_name='İlgili Müşteri')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('order_line', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_line', to='order.order', verbose_name='Sipariş')),
                ('order_line_stock', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_line_stock', to='stock.stock', verbose_name='Stok')),
                ('order_line_unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_line_unit', to='stock.stockunit', verbose_name='Birim')),
                ('order_line_currency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_line_currency', to='order.orderlinecurrency', verbose_name='Para Birimi')),
            ],
            options={
                'verbose_name': 'Sipariş Satırı',
                'verbose_name_plural': 'Sipariş Satırları',
            },
            bases=('core.base',),
        ),
    ]