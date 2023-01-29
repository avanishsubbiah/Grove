from django.db import models
from django.contrib.admin import register
from django.contrib import admin
from users.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db.models import Q
from typing import List
from users.serializers import UserSerializer
from rest_framework.response import Response


class Grove(models.Model):
    user_a = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_a")
    user_b = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_b")
    xp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    start_date = models.DateField(default=timezone.now)

    def get_friends(user: User) -> List[User]:
        friends = []
        for pair in Grove.objects.filter(Q(user_a=user) | Q(user_b=user)).all():
            if pair.user_a.id == user.id:
                friends.append(pair.user_b)
            else:
                friends.append(pair.user_a)
        return friends

    def get_grove(user: User, other: User):
        return Grove.objects.filter(Q(user_a=user, user_b=other) | Q(user_a=other, user_b=user)).first()

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.user_a} - {self.user_b}"


@register(Grove)
class GroveAdmin(admin.ModelAdmin):
    pass
