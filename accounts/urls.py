
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views  

app_name = "accounts"

urlpatterns = [
    # perfil
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),

    # auth básicas propias 
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),

    # cambio de contraseña (built‑in)
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change.html",
            success_url="/accounts/password_change/done/",
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
    ),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
