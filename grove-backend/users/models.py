from django.db import models
from django.db.models import QuerySet


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def get_groves(self) -> QuerySet:
        return self.grove_set.all()

