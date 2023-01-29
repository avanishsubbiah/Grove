from rest_framework import serializers
from .models import UserChallenge, DailyChallenge


class UserChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChallenge
        fields = ["src", "dst", "xp", "desc"]


class DailyChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyChallenge
        fields = ["xp", "desc"]
