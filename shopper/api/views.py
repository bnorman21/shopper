from django.shortcuts import render
from rest_framework import generics
from .serializers import StoreSerializer
from .models import Store

# Create your views here.
class StoreView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
