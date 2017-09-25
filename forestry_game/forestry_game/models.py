from django.db import models
from django.contrib.auth.models import User

# custom user for additional stuff later
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    # django model prvides username, password and email

    def __str__(self):
        return self.user.username

# actual map in the game
class Map(models.Model):
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)

    # model is missing graph information and other stuff (will be defined later)

# result from a single run in the game
class Execution(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(CustomUser)
    map = models.ForeignKey(Map)
