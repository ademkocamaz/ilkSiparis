from django.db import models
from core.models import Base


class StockUnit(Base):
    name = models.CharField(
        verbose_name="Birim Adı",
        max_length=500,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Stok Birimi"
        verbose_name_plural = "Stok Birimleri"
