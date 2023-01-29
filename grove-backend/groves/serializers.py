
from rest_framework import serializers
from .models import Grove


class GroveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grove
        fields = ["username", "first_name", "last_name"]