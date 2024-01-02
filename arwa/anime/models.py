from django.db import models

# Create your models here.
class Anime(models.Model):
  title = models.CharField(max_length=100)
  creator = models.CharField(max_length=100, blank=True)
  rating = models.FloatField(max_value=10.0, min_value=0.0)
  episodes = models.IntegerField(min_value=0)
  aired = models.DateField()
  ended = models.DateField()
  # genres

  def __str__(self) -> str:
    return self.title