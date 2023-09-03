from django.db import models

class station(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Trip(models.Model):
    origin = models.ForeignKey(station, on_delete=models.CASCADE, related_name="departure")
    destination = models.ForeignKey(station, on_delete=models.CASCADE, related_name="arrival")
    duration = models.IntegerField()

    def __str__(self):
        return f"From: {self.origin} To: {self.destination}"
    
class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    trip = models.ManyToManyField(Trip, blank=True, related_name="passenger")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"