from django.urls import path
from user import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("reset_password", views.reset_password, name="reset_password"),
]
