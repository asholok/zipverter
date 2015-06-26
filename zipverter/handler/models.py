from django.db import models

class LocationTable(models.Model):
    class Meta:
        unique_together = (('country', 'zip_code'), )

    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

    def __unicode__(self):
        return self.city

