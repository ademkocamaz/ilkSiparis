from django.urls import path
from order import views

urlpatterns = [
    path(route="", view=views.order, name="order"),
    path(route="<int:pk>/detail/", view=views.OrderDetailView.as_view(), name="order_detail"),
    path(route="create/", view=views.OrderCreateView.as_view(), name="order_create"),
    path(route="<int:order_pk>/print/", view=views.order_print, name="order_print"),
    path(route="order_state/", view=views.order_state, name="order_state"),
    path(route="order_state/<int:order_state_id>/detail", view=views.order_state, name="order_state_detail"),
    path(route="order_line_currency/", view=views.order_line_currency, name="order_line_currency"),
    path(route="order_line_currency/<int:order_line_currency_id>/detail", view=views.order_line_currency_detail, name="order_line_currency_detail"),
]
