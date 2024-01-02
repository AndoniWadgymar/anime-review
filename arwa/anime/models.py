from django.db import models

# Create your models here.
class Anime(models.Model):
  title = models.CharField(max_length=100)
  creator = models.CharField(max_length=100, blank=True)
  rating = models.FloatField()
  episodes = models.IntegerField()
  aired = models.DateField()
  ended = models.DateField()
  # genres

  def __str__(self) -> str:
    return self.title