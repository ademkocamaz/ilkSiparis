from django.db import models
from core.models import Base
from current._model.current import Current
from order._model.order_state import OrderState
from datetime import datetime


class Order(Base):

    current = models.ForeignKey(
        verbose_name="Cari",
        to=Current,
        on_delete=models.CASCADE,
        name="order_current",
        related_name="order_current",
    )

    date = models.DateTimeField(
        verbose_name="Tarih",
        default=datetime.now(),
    )

    shipment_date = models.DateTimeField(
        verbose_name="Sevk Tarihi",
        blank=True,
        null=True,
    )

    invoice_number = models.CharField(
        verbose_name="Fatura No",
        max_length=500,
        blank=True,
        null=True,
    )

    number = models.CharField(
        verbose_name="Sipariş No",
        max_length=500,
        blank=True,
        null=True,
    )

    state = models.ForeignKey(
        verbose_name="Sipariş Durumu",
        to=OrderState,
        on_delete=models.DO_NOTHING,
        name="order_state",
        related_name="order_state",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.current) + " - " + str(self.date) + " - " + str(self.number)

    class Meta:
        verbose_name = "Sipariş"
        verbose_name_plural = "Siparişler"
