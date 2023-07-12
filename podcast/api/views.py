from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import CategorySerializers, TagSerializers, SeasonSerializer
from ..models import Category, Tag, Season


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class SeasonListCreateView(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

