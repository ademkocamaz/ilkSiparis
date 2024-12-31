from django.db import models
from core.models import Base

class StockCategory(Base):
    name = models.CharField(
        verbose_name="Kategori Adı",
        max_length=500,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Stok Kategorisi"
        verbose_name_plural="Stok Kategorileri"