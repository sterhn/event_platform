from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, RegisterForEventView, EventUpdateView

router = DefaultRouter()
router.register('event', EventViewSet, basename='event')
router.register('event-register', RegisterForEventView, basename='event-attender')

urlpatterns = [
    path('', include(router.urls)),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit')
]