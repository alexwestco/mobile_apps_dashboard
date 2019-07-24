from rest_framework import serializers
from hello.models import AppDownload

class AppDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppDownload
        fields = '__all__'