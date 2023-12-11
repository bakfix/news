from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from django.shortcuts import render

class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

