from django.db import models
class bookings(models.Model):
    EventName=models.CharField(max_length=200,default="John Doe")
    Venue=models.CharField(max_length=1,default="NULL")
    Room=models.CharField(max_length=6,default="Null")
    Date=models.DateField()
    Starttime=models.TimeField()
    endtime=models.TimeField()

