from django.db import models
from core.models import Base
from stock._model.stock_unit import StockUnit
from stock._model.stock_type import StockType
from stock._model.stock_model import StockModel
from stock._model.stock_color import StockColor
from stock._model.stock_category import StockCategory
from stock._model.stock_tax_set import StockTaxSet


class Stock(Base):
    name = models.CharField(
        verbose_name="Adı",
        max_length=500,
    )

    barcode = models.CharField(
        verbose_name="Barkod",
        max_length=500,
        blank=True,
        null=True,
    )

    model = models.ForeignKey(
        verbose_name="Model",
        to=StockModel,
        on_delete=models.DO_NOTHING,
        name="stock_model",
        related_name="stock_model",
        blank=True,
        null=True,
    )

    color = models.ForeignKey(
        verbose_name="Renk",
        to=StockColor,
        on_delete=models.DO_NOTHING,
        name="stock_color",
        related_name="stock_color",
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        verbose_name="Kategori",
        to=StockCategory,
        on_delete=models.DO_NOTHING,
        name="stock_category",
        related_name="stock_category",
        blank=True,
        null=True,
    )

    unit = models.ForeignKey(
        verbose_name="Birim",
        to=StockUnit,
        on_delete=models.CASCADE,
        name="stock_unit",
        related_name="stock_unit",
    )

    type = models.ForeignKey(
        verbose_name="Tipi",
        to=StockType,
        on_delete=models.CASCADE,
        name="stock_type",
        related_name="stock_type",
        blank=True,
        null=True,
    )

    tax_set = models.ForeignKey(
        verbose_name="Vergi Seti",
        to=StockTaxSet,
        on_delete=models.DO_NOTHING,
        name="stock_tax_set",
        related_name="stock_tax_set",
        blank=True,
        null=True,
    )

    purchase_price = models.DecimalField(
        verbose_name="Alış Fiyatı",
        max_digits=20,
        decimal_places=2,
        blank=True,
        null=True,
    )

    sales_price = models.DecimalField(
        verbose_name="Satış Fiyatı",
        max_digits=20,
        decimal_places=2,
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
        return (
            self.name
            + " - Model: "
            + str(self.stock_model)
            + " - Renk: "
            + str(self.stock_color)
            + " - Kategori: "
            + str(self.stock_category)
            + " - Tipi: "
            + str(self.type)
        )

    class Meta:
        verbose_name = "Stok Kartı"
        verbose_name_plural = "Stok Kartları"
