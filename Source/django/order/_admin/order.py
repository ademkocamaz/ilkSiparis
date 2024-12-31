from django.contrib import admin
from order._model.order import Order
from order._admin.order_line import OrderLineInline

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields if field.name not in ("base_ptr_id")]
    list_display_links = [field.name for field in Order._meta.fields if field.name not in ("base_ptr_id")]
    search_fields = [field.name for field in Order._meta.fields if field.name not in ("base_ptr_id")]
    readonly_fields = [
        "user",
    ]

    save_on_top = True

    inlines=[
        OrderLineInline
    ]

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()
