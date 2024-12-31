from django.db import models
from core.models import Base


class Current(Base):

    name = models.CharField(
        verbose_name="Müşteri/Firma Adı",
        max_length=500,
    )

    title1 = models.CharField(
        verbose_name="Ünvan 1",
        max_length=500,
        blank=True,
        null=True,
    )

    title2 = models.CharField(
        verbose_name="Ünvan 2",
        max_length=500,
        blank=True,
        null=True,
    )

    tax_id = models.CharField(
        verbose_name="Vergi No",
        max_length=500,
        blank=True,
        null=True,
    )

    tax_authority = models.CharField(
        verbose_name="Vergi Dairesi",
        max_length=500,
        blank=True,
        null=True,
    )

    phone = models.CharField(
        verbose_name="Telefon",
        max_length=500,
        blank=True,
        null=True,
    )

    address = models.TextField(
        verbose_name="Adres",
        blank=True,
        null=True,
    )

    description = models.TextField(
        verbose_name="Açıklama",
        blank=True,
        null=True,
    )

    note = models.TextField(
        verbose_name="Not",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cari Kartı"
        verbose_name_plural = "Cari Kartları"


