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
    gas_consumption = models.FloatField(default=0)
    duration = models.IntegerField(default=0)
    logs = models.TextField(default="")
    user = models.ForeignKey(User)
    level = models.ForeignKey(Level)

    #For detailed report
    driving_unloaded_time = models.IntegerField(default=0)
    loading = models.IntegerField(default=0)
    driving_loaded_time = models.IntegerField(default=0)
    unloading = models.IntegerField(default=0)
    idling = models.IntegerField(default=0)

    driving_forward = models.IntegerField(default=0)
    reverse = models.IntegerField(default=0)
    driving_unloaded_distance = models.IntegerField(default=0)
    driving_loaded_distance = models.IntegerField(default=0)

    fuel_cost = models.FloatField(default=0)
    worker_salary = models.IntegerField(default=0)

    loads_transported = models.IntegerField(default=0)
    productivity = models.FloatField(default=0)

    def score(self):
        SALARY = 20
        DIESEL_PRICE = 1.2
        HOUR = 3600
        
        salary = SALARY / HOUR * self.duration
        gas_price = DIESEL_PRICE * self.gas_consumption

        return str("%0.2f" % (salary + gas_price))

    def __str__(self):
        return self.user.username + ' - ' + str(self.score()) + ' - ' + str(self.pk)
