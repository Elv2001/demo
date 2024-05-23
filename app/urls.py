from django.urls import path
from .views import LogoutView, app_admin, addstatement, register, LoginView, statements

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", register, name="register"),
    path("statements/", statements, name="statements"),
    path("addstatement/", addstatement, name="addstatement"),
    path("app_admin/", app_admin, name="app_admin"),
]
