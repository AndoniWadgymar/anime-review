from rest_framework import serializers

from anime.models import Creator, Anime

class CreatorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Creator
    fields = "__all__"

class AnimeSerializer(serializers):
  class Meta:
    model = Anime
    fields = "__all__"