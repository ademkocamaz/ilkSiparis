from django.urls import path
from stock import views
urlpatterns = [
    path(route="", view=views.stock, name="stock"),
    path(route="<int:stock_id>/detail", view=views.stock_detail, name="stock_detail"),

    path(route="stock_unit/", view=views.stock_unit, name="stock_unit"),
    path(route="stock_unit/<int:stock_unit_id>/detail", view=views.stock_unit_detail, name="stock_unit_detail"),

    path(route="stock_type/", view=views.stock_type, name="stock_type"),
    path(route="stock_type/<int:stock_type_id>/detail", view=views.stock_type_detail, name="stock_type_detail"),
    
    path(route="stock_tax_set/", view=views.stock_tax_set, name="stock_tax_set"),
    path(route="stock_tax_set/<int:stock_tax_set_id>/detail", view=views.stock_tax_set_detail, name="stock_tax_set_detail"),
    
    path(route="stock_model/", view=views.stock_model, name="stock_model"),
    path(route="stock_model/<int:stock_model_id>/detail", view=views.stock_model_detail, name="stock_model_detail"),

    path(route="stock_color/", view=views.stock_color, name="stock_color"),
    path(route="stock_color/<int:stock_color_id>/detail", view=views.stock_color_detail, name="stock_color_detail"),
    
    path(route="stock_category/", view=views.stock_category, name="stock_category"),
    path(route="stock_category/<int:stock_category_id>/detail", view=views.stock_category_detail, name="stock_category_detail"),






]
