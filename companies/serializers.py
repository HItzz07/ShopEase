from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.Serializer):
    class Meta:
        model = Company
        fields = ["id", "name", "owner", "created_at"]
        read_only_fields = ["owner", "created_at"]