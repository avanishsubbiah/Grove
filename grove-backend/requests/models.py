from django.db import models
from users.models import User
from django.contrib import admin
from django.contrib.admin import register


class Request(models.Model):
    src = models.ForeignKey(User, on_delete=models.CASCADE, related_name="src")
    dst = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dst")
    desc = models.CharField(default="", max_length=255)

    def __repr__(self) -> str:
        return f"{self.src} requested to be friends with {self.dst}"


@register(Request)
class RequestAdmin(admin.ModelAdmin):
    pass