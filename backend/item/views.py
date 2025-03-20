from unicodedata import lookup

from bson import ObjectId
from django.shortcuts import render

from google import genai

# Create your views here

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics

from .models import Item
from .serializers import ItemSerializer, ItemListSerializer, UserItemsSerializer


class ItemUploadView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ItemSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





from rest_framework_mongoengine import generics as drfme_generics
class ItemDetailView(drfme_generics.RetrieveAPIView):
    queryset = Item.objects.all()
    lookup_field = 'id'
    serializer_class = ItemListSerializer

class UserItemsView(drfme_generics.ListAPIView):
    queryset = Item.objects.all()
    lookup_field = 'user'
    serializer_class = UserItemsSerializer
    def get_queryset(self):
        # Filter items that belong to the current user
        return Item.objects.filter(user=self.request.user)





