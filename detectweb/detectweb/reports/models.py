from django.db import models

# Create your models here.
class Report(models.Model):
    # Length 36 uuid.
    image_file = models.CharField(max_length=50, unique=True)
