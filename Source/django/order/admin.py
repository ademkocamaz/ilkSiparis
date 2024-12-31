from django.contrib import admin

# Register your models here.

from order._admin.order import OrderAdmin
from order._admin.order_line import OrderLineAdmin
from order._admin.order_state import OrderStateAdmin
from order._admin.order_line_currency import OrderLineCurrencyAdmin
