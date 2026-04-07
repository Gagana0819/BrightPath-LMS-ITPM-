from django.urls import path
from .views import RegisterView, LoginView, ResetPasswordView, OCRScanView, UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('ocr-scan/', OCRScanView.as_view(), name='ocr_scan'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
