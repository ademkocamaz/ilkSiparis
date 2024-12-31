from django.contrib import admin

# Register your models here.

from stock._admin.stock import StockAdmin
from stock._admin.stock_category import StockCategoryAdmin
from stock._admin.stock_color import StockColorAdmin
from stock._admin.stock_model import StockModelAdmin
from stock._admin.stock_tax_set import StockTaxSetAdmin
from stock._admin.stock_type import StockTypeAdmin
from stock._admin.stock_unit import StockUnitAdmin