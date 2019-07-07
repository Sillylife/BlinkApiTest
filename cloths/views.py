from django.shortcuts import render
from .models import AllClothes
from rest_framework import generics
from .serializers import AllClothesSerializer
# Create your views here.

class cothList(generics.ListCreateAPIView):
    queryset = AllClothes.objects.all()
    serializer_class = AllClothesSerializer
