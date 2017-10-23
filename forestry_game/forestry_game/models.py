from django.db import models
from django.contrib.auth.models import User

# custom user for additional stuff later
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    # django model prvides username, password and email

    def __str__(self):
        return self.user.username

# actual map in the game
class Level(models.Model):
    name = models.CharField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(CustomUser)

    def __str__(self):
        return self.name + ' - ' + self.creator + ' - ' + str(self.pk)

# result from a single run in the game
class Report(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    distance = models.IntegerField(default=0)
    gas_consumption = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    logs = models.TextField(default="")
    user = models.ForeignKey(CustomUser)
    level = models.ForeignKey(Level)

    def score(self):
        return self.distance * self.gas_consumption * self.duration

    def __str__(self):
        return self.user.username + ' - ' + self.score + ' - ' + str(self.pk)