from rest_framework import serializers
from .models import Profile

from rest_framework_mongoengine.serializers import DocumentSerializer

class ProfileSerializer(DocumentSerializer):
  class Meta:
    model = Profile
    fields = ['id', 'username', 'gender', 'email']
    read_only_fields = ['id', 'date_joined', 'updated_at']