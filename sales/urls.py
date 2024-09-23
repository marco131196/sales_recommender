from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SalesAlgorithmViewSet,
    UploadedDatasetViewSet,
    SalesRecommendationResultViewSet,
)

router = DefaultRouter()
router.register(r'sales-algorithms', SalesAlgorithmViewSet)
router.register(r'upload-dataset', UploadedDatasetViewSet)
router.register(r'results', SalesRecommendationResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]