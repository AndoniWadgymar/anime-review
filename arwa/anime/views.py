from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from anime.models import Creator, Anime
from anime.serializer import CreatorSerializer, AnimeSerializer

# Create your views here.
class CreatorViewSet(viewsets.ViewSet):
  """
  A simple viewset for viewing all categories
  """
  queryset = Creator.objects.all()

  @extend_schema(responses=CreatorSerializer)
  def list(self, request):
    serializer = CreatorSerializer(self.queryset, many=True)
    return Response(serializer.data)