# Generated by Django 5.1.4 on 2024-12-31 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_category', to='stock.stockcategory', verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_color', to='stock.stockcolor', verbose_name='Renk'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_model', to='stock.stockmodel', verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_tax_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_tax_set', to='stock.stocktaxset', verbose_name='Vergi Seti'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_type', to='stock.stocktype', verbose_name='Tipi'),
        ),
    ]
