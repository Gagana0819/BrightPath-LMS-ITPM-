from django.urls import path
from .views import ResourceUploadView, ResourceListView

urlpatterns = [
    path('resources/upload/', ResourceUploadView.as_view(), name='resource-upload'),
    path('resources/', ResourceListView.as_view(), name='resource-list'),
]
