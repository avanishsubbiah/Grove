from django.db import models
from django.contrib.admin import register
from django.contrib import admin
from users.models import User


class Grove(models.Model):
    user_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_a")
    user_b = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_b")
    xp = models.IntegerField()
    start_date = models.DateField()

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.user_a} - {self.user_b}"


@register(Grove)
class GroveAdmin(admin.ModelAdmin):
    pass
