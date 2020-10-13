from django.contrib import admin
from .models import Images


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
	fields = ['image', 'image_url', 'image_resized', 'width', 'heigth']
