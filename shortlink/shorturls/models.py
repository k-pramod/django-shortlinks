from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Shortlink(models.Model):  # class Shortlink extends/implements Models
    long_url = models.CharField(max_length=256, blank=False)
    short_id = models.CharField(max_length=4, blank=False)

    def __str__(self):
        return self.short_id.__str__() + " --> " + self.long_url.__str__()
