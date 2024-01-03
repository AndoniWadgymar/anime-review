import factory
from factory.faker import faker

from anime.models import Anime, Creator

class CreatorFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Creator

  name = "Eiichirō Oda"

class AnimeFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Anime

  title = "One Piece"
  creator = factory.SubFactory(CreatorFactory)
  rating = 10.0
  episodes = 1100
  aired = factory.Faker("date_this_century")
  ended = factory.Faker("date_this_month")