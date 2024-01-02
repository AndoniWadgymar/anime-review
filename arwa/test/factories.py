from factory import DjangoModelFactory, Faker

from anime.models import Anime

class AnimeFactory(DjangoModelFactory):
  title = Faker("title")
  creator = Faker("name")
  rating = Faker("random_int")
  episodes = Faker("random_int")
  aired = Faker('date_time_this_decade')
  ended = Faker('date_time_this_month')

  class Meta:
    model = Anime
