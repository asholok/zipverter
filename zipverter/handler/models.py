from django.db import models

class LocationTable(models.Model):
    class Meta:
        unique_together = (('country', 'zip_code'), )

    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

    def __unicode__(self):
        return self.city

class LoggForLocationTable(models.Model):
    request = models.CharField(max_length=200)
    response = models.CharField(max_length=200)
    client_ip = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '{}___{}'.format(self.client_ip, self.date)
