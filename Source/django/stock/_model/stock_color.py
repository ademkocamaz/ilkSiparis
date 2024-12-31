from django.db import models
from core.models import Base

class StockColor(Base):
    name = models.CharField(
        verbose_name="Renk Adı",
        max_length=500,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Stok Rengi"
        verbose_name_plural="Stok Renkleri"