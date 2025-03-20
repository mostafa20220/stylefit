from django.urls import path
from .views import ItemUploadView, ItemDetailView, UserItemsView

urlpatterns = [
    path('' , UserItemsView.as_view(), name='user-items'),
    path('upload/', ItemUploadView.as_view(), name='item-upload'),
    path('<str:id>/', ItemDetailView.as_view(), name='item-detail'),
]