from django.shortcuts import render
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import Event, EventAttender
from .serializers import EventSerializer, EventAttenderSerializer
from .permissions import IsAdminOrReadOnly, IsEventPlanner

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminOrReadOnly, IsEventPlanner]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['date', 'start_time']
    search_fields = ['name', 'type']
    ordering_fields = ['date', 'start_time']

class RegisterForEventView(viewsets.ModelViewSet):
    queryset = EventAttender.objects.all()
    serializer_class = EventAttenderSerializer