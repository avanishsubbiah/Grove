from django.db import models
from django.db.models import QuerySet
from grooves.model import Grove


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def get_groves(self) -> QuerySet:
        return self.grove_set.all()

    def get_grove(self, other: User) -> Grove:
