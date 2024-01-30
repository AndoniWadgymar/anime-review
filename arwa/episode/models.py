from django.db import models
from anime import models

# Create your models here.
class Episode(models.Model):
  title = models.CharField(max_length=100, null=False, blank=False)
