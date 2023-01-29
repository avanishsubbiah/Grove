from django.db import models
from users.models import User


# Create your models here.
class Grove(models.Model):
    user_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_a")
    user_b = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_b")
    xp = models.IntegerField()
    start_date = models.DateField()
