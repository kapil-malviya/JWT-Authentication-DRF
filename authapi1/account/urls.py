from django.urls import path
from account.views import *   # UserRegistrationView, UserLogin, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<user_id>/<token>', UserPasswordResetView.as_view(), name='reset-password'),
]