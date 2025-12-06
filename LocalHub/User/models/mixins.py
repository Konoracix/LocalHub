from django.db import models
import math

class TimeStampesMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class LocationMixin(models.Model):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location_name = models.CharField(max_length=100, null=True, blank=True)

    def get_distance(self, lat, lon):
        dlat = math.radians(self.latitude) - math.radians(lat)
        dlon = math.radians(self.longitude) - math.radians(lon)
        a = (math.sin(dlat/2) ** 2) + math.cos(self.latitude) * math.cos(lat) * (math.sin(dlon/2) ** 2)
        c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
        return round(c * 6371, 3)


    class Meta:
        abstract = True