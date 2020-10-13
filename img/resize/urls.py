from django.urls import path
from .views import HomeView, UploadImage, DetailImage


urlpatterns = [
	path('',HomeView.as_view(), name = 'home'),
	path('upload/', UploadImage.as_view(), name = 'upload'),
	path('image/<int:pk>/image_edit/',DetailImage.as_view(), name = 'image_edit')
]
