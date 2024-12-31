from django.db import models
from core.models import Base

class StockModel(Base):
    name = models.CharField(
        verbose_name="Model Adı",
        max_length=500,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Stok Modeli"
        verbose_name_plural="Stok Modelleri"