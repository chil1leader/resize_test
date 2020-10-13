from django.shortcuts import redirect

from .forms import ImageForm, ResizedForm
from django.views.generic import ListView, CreateView, UpdateView
from .models import Images


class HomeView(ListView):
	model = Images
	template_name = 'home.html'

class UploadImage(CreateView):
	model = Images
	form_class = ImageForm
	template_name = 'upload.html'
	def get_success_url(self):
		url = self.object.get_absolute_url()
		return url


class DetailImage(UpdateView):
	model = Images
	form_class = ResizedForm
	template_name = 'image_edit.html'
	context_object_name = 'image'
	def get_success_url(self):
		url = self.object.get_absolute_url()
		return url
	def red(self):
		return redirect('upload')











