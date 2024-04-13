from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'users'

urlpatterns = [
    # url-адреса входа и выхода
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),


    # url-адреса смены пароля
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),


    # url-адреса сброса пароля
    path(
        "password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),

    
    path("register/", views.register, name="register"),
    path("profile/", views.ProfileUser.as_view(), name="profile"),
]
