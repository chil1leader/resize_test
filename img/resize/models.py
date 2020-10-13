from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from django.core.files import File
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from PIL import Image
import os.path
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.images import get_image_dimensions


upload_path = 'images'
upload_path_resized = 'resized'



class Images(models.Model):
    image = models.ImageField(upload_to=upload_path, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image_resized = models.ImageField(upload_to=upload_path_resized,blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    heigth = models.PositiveIntegerField(null=True, blank=True)

    def clean(self):
        if (self.image == None and self.image_url == None ) or (self.image != None and self.image_url != None ):
            raise ValidationError('Empty or both blanked')

    def get_absolute_url(self):
        return reverse('image_edit', args=[str(self.id)])



    def save(self):
        if self.image_url and not self.image:
            name = str(self.image_url).split('/')[-1]
            img = NamedTemporaryFile(delete=True)
            img.write(urlopen(self.image_url).read())
            img.flush()
            self.image.save(name, File(img))
            self.image_url = None
        if self.image and not self.image_resized:
            self.resize()
        return super(Images, self).save()

    def resize(self):
        if self.width or self.heigth:
            output_size = self.width, self.heigth
            img = Image.open(self.image)
            img.thumbnail(output_size)
            thumb_name, thumb_extension = os.path.splitext(self.image.name)
            thumb_extension = thumb_extension.lower()
            thumb_filename = thumb_name + '_thumb' + thumb_extension
            if thumb_extension in ['.jpg', '.jpeg']:
                FTYPE = 'JPEG'
            elif thumb_extension == '.gif':
                FTYPE = 'GIF'
            elif thumb_extension == '.png':
                FTYPE = 'PNG'
            else:
                return False
            temp_thumb = BytesIO()
            img.save(temp_thumb, FTYPE)
            temp_thumb.seek(0)
            self.image_resized.save(thumb_filename, ContentFile(temp_thumb.read()))
            temp_thumb.close()
















































