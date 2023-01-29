from django.db import models
from users.models import User


class Quest(models.Model):
    decription = models.CharField(max_length=1024)
    status = models.BooleanField()
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_to")
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_from")
    exp = models.IntegerField()