from django.contrib import admin
from order._model.order_line import OrderLine


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderLine._meta.fields if field.name not in ("base_ptr_id")]
    list_display_links = [field.name for field in OrderLine._meta.fields if field.name not in ("base_ptr_id")]
    search_fields = [field.name for field in OrderLine._meta.fields if field.name not in ("base_ptr_id")]
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


class OrderLineInline(admin.StackedInline):
    model = OrderLine
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)
    readonly_fields = [
        "user",
    ]
    fk_name = "order_line"
