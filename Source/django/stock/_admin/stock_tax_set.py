from django.contrib import admin
from stock._model.stock_tax_set import StockTaxSet


@admin.register(StockTaxSet)
class StockTaxSetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StockTaxSet._meta.fields if field.name not in ("base_ptr_id")]
    list_display_links = [field.name for field in StockTaxSet._meta.fields if field.name not in ("base_ptr_id")]
    search_fields = [field.name for field in StockTaxSet._meta.fields if field.name not in ("base_ptr_id")]
    readonly_fields = [
        "user",
    ]

    save_on_top = True

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()