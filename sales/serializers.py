from rest_framework import serializers
from .models import SalesAlgorithm, UploadedDataset, SalesRecommendationResult

class SalesAlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesAlgorithm
        fields = '__all__'

class UploadedDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedDataset
        fields = '__all__'

class SalesRecommendationResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRecommendationResult
        fields = '__all__'
