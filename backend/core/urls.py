from django.urls import path
from .views import (
    ResourceUploadView, ResourceListView,
    KuppiSessionListCreateView, KuppiSessionDetailView,
    KuppiSessionVideoUploadView, KuppiSessionIncrementViews,
    KuppiSessionThumbnailUploadView,
    RecordResourceDownloadView, ResourceReviewCreateView,
    ResourceReviewListView, ResourceRatingStatsView
)

urlpatterns = [
    path('resources/upload/', ResourceUploadView.as_view(), name='resource-upload'),
    path('resources/', ResourceListView.as_view(), name='resource-list'),
    
    # Kuppi Sessions
    path('kuppi/sessions/', KuppiSessionListCreateView.as_view(), name='kuppi-session-list-create'),
    path('kuppi/sessions/<int:pk>/', KuppiSessionDetailView.as_view(), name='kuppi-session-detail'),
    path('kuppi/sessions/<int:pk>/upload-video/', KuppiSessionVideoUploadView.as_view(), name='kuppi-session-upload-video'),
    path('kuppi/sessions/<int:pk>/increment-views/', KuppiSessionIncrementViews.as_view(), name='kuppi-session-increment-views'),
    path('kuppi/sessions/<int:pk>/upload-thumbnail/', KuppiSessionThumbnailUploadView.as_view(), name='kuppi-session-upload-thumbnail'),
    
    # Resource Reviews & Downloads
    path('resources/<int:pk>/record-download/', RecordResourceDownloadView.as_view(), name='resource-record-download'),
    path('resources/<int:pk>/reviews/', ResourceReviewListView.as_view(), name='resource-review-list'),
    path('resources/<int:pk>/stats/', ResourceRatingStatsView.as_view(), name='resource-rating-stats'),
    path('resources/reviews/add/', ResourceReviewCreateView.as_view(), name='resource-review-create'),
]
