from django.forms import ModelForm
from .models import Images

class ImageForm(ModelForm):
	class Meta:
		model = Images
		fields = ['image', 'image_url']

class ResizedForm(ModelForm):
	class Meta:
		model = Images
		fields = ['width', 'heigth']







