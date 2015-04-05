from django.db import models
import uuid

def uploaded_file_name(instance, filename):
  return '/'.join(['uploaded_images', str(uuid.uuid4()), filename]);

# Create your models here.
class Report(models.Model):
  # Length 36 uuid.
  image_file = models.FileField(upload_to=uploaded_file_name)
  is_finished = models.BooleanField(default=False)
