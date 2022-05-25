from rest_framework import serializers
from .models import jobApplication

class jobAppliedSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobApplication
        fields = "__all__"