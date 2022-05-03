from django.db import models
class bookings(models.Model):
    EventName=models.CharField(max_length=200,default="John Doe")
    Venue=models.CharField(max_length=1,null=False)
    Room=models.CharField(max_length=6,null=False)
    Date=models.DateField(null=False)
    Starttime=models.TimeField(null=False)
    endtime=models.TimeField(null=False)

