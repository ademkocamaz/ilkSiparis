from django.db import models
from core.models import Base


class OrderState(Base):

    name = models.CharField(
        verbose_name="Adı",
        max_length=500,
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Sipariş Durumu"
        verbose_name_plural="Sipariş Durumları"
