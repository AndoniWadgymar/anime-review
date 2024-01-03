from django.db import models

# Create your models here.
class Creator(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self) -> str:
    return self.name

class Anime(models.Model):
  title = models.CharField(max_length=100)
  creator = models.ForeignKey(Creator, related_name='creator', on_delete=models.DO_NOTHING, null=True, blank=True)
  rating = models.FloatField()
  episodes = models.IntegerField()
  aired = models.DateField()
  ended = models.DateField()
  # genres

  def __str__(self) -> str:
    return self.title