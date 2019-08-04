from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from crm_system.crm_food.serializers import *
from .models import *
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    def perform_create(self, serializer):
        serializer.save()
