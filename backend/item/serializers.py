from bson import ObjectId
from django.contrib.auth.middleware import get_user
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework_mongoengine.serializers import DocumentSerializer


from .models import Item
import cloudinary.uploader
from rest_framework import serializers
from .models import Item
import jwt
from django.conf import settings

from .utils import item_generator


class ItemSerializer(DocumentSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(source="user.id", read_only=True)  # Serialize user as an ID
    category = serializers.CharField(source="category.value", read_only=True)
    color = serializers.CharField(read_only=True)
    season = serializers.CharField(source="season.value", read_only=True)
    type = serializers.CharField(source="type.value", read_only=True)
    pattern = serializers.CharField(read_only=True)
    material = serializers.CharField(read_only=True)
    description = serializers.CharField(allow_null=True, required=False)
    image = serializers.ImageField(write_only=True)  # Use URLField for the image URL

    def create(self, validated_data):
        user_id = self.context["request"].user_id
        image = validated_data.pop("image")

        # Upload image to Cloudinary
        upload_result = cloudinary.uploader.upload(image)
        image_url = upload_result["secure_url"]

        newItem = item_generator(image, image_url, user_id)


        # Create ClothingItem with default values
        clothing_item = Item(**newItem)
        clothing_item.save()
        return clothing_item


class ItemListSerializer(DocumentSerializer):

    class Meta:
        model = Item
        fields = '__all__'

class UserItemsSerializer(DocumentSerializer):
    class Meta:
        model = Item
        fields = '__all__'