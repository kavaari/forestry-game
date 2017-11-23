from django.db import models
from django.contrib.auth.models import User

# actual map in the game
class Level(models.Model):
    name = models.CharField(default="", max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    mapdata = models.TextField(default="")
    mapinfo = models.TextField(default="")
    creator = models.ForeignKey(User)

    def __str__(self):
        return self.name + ' - ' + self.creator.username + ' - ' + str(self.pk)


# result from a single run in the game
class Report(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    distance = models.IntegerField(default=0)
    gas_consumption = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    logs = models.TextField(default="")
    user = models.ForeignKey(User)
    level = models.ForeignKey(Level)

    def score(self):
        return self.distance * self.gas_consumption * self.duration

    def __str__(self):
        return self.user.username + ' - ' + str(self.score()) + ' - ' + str(self.pk)
