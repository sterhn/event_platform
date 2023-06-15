from rest_framework import serializers

from .models import Event, EventAttender


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventAttenderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.CharField(source='user.username', read_only=True)
    event = serializers.CharField(source='event.name')  # Use the 'name' field of the related event model

    class Meta:
        model = EventAttender
        fields = '__all__'
        extra_fields = ['username', 'event_name']
        