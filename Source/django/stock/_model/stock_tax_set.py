from django.db import models
from core.models import Base


class StockTaxSet(Base):
    name = models.CharField(
        verbose_name="Adı",
        max_length=500,
    )

    rate = models.DecimalField(
        verbose_name="Vergi Oranı",
        max_digits=5,
        decimal_places=2,
    )

    def __str__(self):
        return self.name + " - %" + str(self.rate)

    class Meta:
        verbose_name = "Stok Vergi Oranı"
        verbose_name_plural = "Stok Vergi Oranları"
