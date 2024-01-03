from pytest_factoryboy import register

from .factories import CreatorFactory, AnimeFactory

register(CreatorFactory)
register(AnimeFactory)