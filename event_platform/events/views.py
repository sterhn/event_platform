from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import Event, EventAttender
from .serializers import EventSerializer, EventAttenderSerializer
from .permissions import IsEventPlannerOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsEventPlannerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['date', 'start_time']
    search_fields = ['name', 'type']
    ordering_fields = ['date', 'start_time']

class RegisterForEventView(viewsets.ModelViewSet):
    queryset = EventAttender.objects.all()
    serializer_class = EventAttenderSerializer

class EventUpdateView(View):
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        context = {'event': event}
        return render(request, 'event_edit.html', context)

    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        event.name = request.POST.get('name')
        event.type = request.POST.get('type')
        event.date = request.POST.get('date')
        event.start_time = request.POST.get('start_time')
        event.save()
        # Redirect to a success page or do any other necessary processing
        context = {'event': event}
        return render(request, 'event_edit.html', context)