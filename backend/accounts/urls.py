from django.urls import path
from .views import RegisterView, LoginView, ResetPasswordView, OCRScanView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('ocr-scan/', OCRScanView.as_view(), name='ocr_scan'),
]
