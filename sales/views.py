from django.shortcuts import render

from rest_framework import viewsets
from .models import SalesAlgorithm, UploadedDataset, SalesRecommendationResult
from .serializers import (
    SalesAlgorithmSerializer,
    UploadedDatasetSerializer,
    SalesRecommendationResultSerializer,
)

class SalesAlgorithmViewSet(viewsets.ModelViewSet):
    queryset = SalesAlgorithm.objects.all()
    serializer_class = SalesAlgorithmSerializer

class UploadedDatasetViewSet(viewsets.ModelViewSet):
    queryset = UploadedDataset.objects.all()
    serializer_class = UploadedDatasetSerializer

class SalesRecommendationResultViewSet(viewsets.ModelViewSet):
    queryset = SalesRecommendationResult.objects.all()
    serializer_class = SalesRecommendationResultSerializer

