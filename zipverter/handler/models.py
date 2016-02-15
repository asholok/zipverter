from django.db import models

class LocationTable(models.Model):
    class Meta:
        unique_together = (('country', 'zip_code'), )

    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    state_code = models.CharField(max_length=7, blank=True)
    district = models.CharField(max_length=100, blank=True)
    timezone = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return self.city

class LoggForLocationTable(models.Model):
    request = models.CharField(max_length=256)
    response = models.CharField(max_length=256)
    client_ip = models.CharField(max_length=256)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '{}___{}'.format(self.client_ip, self.date)
