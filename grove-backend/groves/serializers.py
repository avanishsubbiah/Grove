from rest_framework import serializers
from .models import Grove


class GroveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grove
        fields = ["id","user_a" ,"user_b", "xp", "start_date"]
