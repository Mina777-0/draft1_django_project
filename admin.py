from django.contrib import admin
from app.models import station, Trip, Passenger

admin.site.register(station)
admin.site.register(Trip)
admin.site.register(Passenger)