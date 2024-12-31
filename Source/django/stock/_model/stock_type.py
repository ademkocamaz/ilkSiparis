from django.db import models
from core.models import Base

class StockType(Base):
    name = models.CharField(
        verbose_name="Adı",
        max_length=500,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Stok Tipi"
        verbose_name_plural="Stok Tipleri"