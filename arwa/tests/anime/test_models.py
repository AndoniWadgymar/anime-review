import pytest

pytestmark = pytest.mark.django_db

class TestCreatorModel:

  def test_str_method(self, creator_factory):
    obj = creator_factory()
    assert obj.__str__() == "Eiichirō Oda"

class TestAnimeModel:

  def test_str_method(self, anime_factory):
    obj = anime_factory()
    assert obj.__str__() == "One Piece"