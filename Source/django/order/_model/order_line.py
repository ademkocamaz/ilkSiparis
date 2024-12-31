from django.db import models
from core.models import Base
from order._model.order import Order
from order._model.order_line_currency import OrderLineCurrency
from stock._model.stock import Stock
from stock._model.stock_unit import StockUnit


class OrderLine(Base):
    order = models.ForeignKey(
        verbose_name="Sipariş",
        to=Order,
        on_delete=models.DO_NOTHING,
        name="order_line",
        related_name="order_line",
    )

    stock = models.ForeignKey(
        verbose_name="Stok",
        to=Stock,
        on_delete=models.DO_NOTHING,
        name="order_line_stock",
        related_name="order_line_stock",
    )

    quantity = models.DecimalField(
        verbose_name="Miktar",
        max_digits=20,
        decimal_places=5,
    )

    unit = models.ForeignKey(
        verbose_name="Birim",
        to=StockUnit,
        on_delete=models.DO_NOTHING,
        name="order_line_unit",
        related_name="order_line_unit",
    )

    unit_price = models.DecimalField(
        verbose_name="Birim Fiyat",
        max_digits=20,
        decimal_places=5,
        blank=True,
        null=True,
        default=0.00,
    )

    total_price = models.DecimalField(
        verbose_name="Toplam Fiyat",
        max_digits=20,
        decimal_places=5,
        blank=True,
        null=True,
        default=0.00,
    )

    currency = models.ForeignKey(
        verbose_name="Para Birimi",
        to=OrderLineCurrency,
        on_delete=models.DO_NOTHING,
        name="order_line_currency",
        related_name="order_line_currency",
    )

    city = models.CharField(
        verbose_name="Şehir",
        max_length=500,
        blank=True,
        null=True,
    )

    country = models.CharField(
        verbose_name="Ülke",
        max_length=500,
        blank=True,
        null=True,
    )

    related_person = models.CharField(
        verbose_name="İlgili Müşteri",
        max_length=500,
        blank=True,
        null=True,
    )

    description = models.TextField(
        verbose_name="Açıklama",
        blank=True,
        null=True,
    )

    def __str__(self):
        return (
            str(self.order)
            + " - "
            + str(self.stock)
            + " - "
            + str(self.quantity)
            + " - "
            + str(self.unit)
        )

    class Meta:
        verbose_name = "Sipariş Satırı"
        verbose_name_plural = "Sipariş Satırları"
