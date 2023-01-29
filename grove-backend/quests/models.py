from django.db import models
from users.models import User
# Create your models here.

class Quest(models.Model):
    decription = models.CharField(max_length=1024)
    status = models.BooleanField()
    user_to = models.ForeignKey(User, on_delete=models.CASCADE)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE)
    exp = models.IntegerField()