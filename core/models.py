from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class Master(models.Model):
    name = models.CharField(max_length=20)
    choice1 = models.BooleanField(default=False)
    choice2 = models.BooleanField(default=False)
    choice3 = models.BooleanField(default=False)
    choice4 = models.BooleanField(default=False)
    choice5 = models.BooleanField(default=False)
    choice6 = models.BooleanField(default=False)
    choice7 = models.BooleanField(default=False)
    choice8 = models.BooleanField(default=False)
    choice9 = models.BooleanField(default=False)
    choice10 = models.BooleanField(default=False)

    # 왼쪽이 True 오른쪽이 False

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=20)
    choice1 = models.BooleanField(default=False)
    choice2 = models.BooleanField(default=False)
    choice3 = models.BooleanField(default=False)
    choice4 = models.BooleanField(default=False)
    choice5 = models.BooleanField(default=False)
    choice6 = models.BooleanField(default=False)
    choice7 = models.BooleanField(default=False)
    choice8 = models.BooleanField(default=False)
    choice9 = models.BooleanField(default=False)
    choice10 = models.BooleanField(default=False)

    # 왼쪽이 True 오른쪽이 False

    def __str__(self):
        return self.name
