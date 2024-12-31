from django.urls import path
from current import views
urlpatterns = [
    path(route="", view=views.current, name="current"),
    path(route="<int:current_id>/detail", view=views.current_detail, name="current_detail"),
]
