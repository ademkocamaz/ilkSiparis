from django.db import models
from core.models import Base


class OrderLineCurrency(Base):
    name = models.CharField(
        verbose_name="Adı",
        max_length=500,
    )

    symbol = models.CharField(
        verbose_name="Sembol",
        max_length=500,
    )

    def __str__(self):
        return self.name + " - " + self.symbol

    class Meta:
        verbose_name = "Para Birimi"
        verbose_name_plural = "Para Birimleri"
