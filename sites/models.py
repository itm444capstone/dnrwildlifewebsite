import re
import alerts
import facilities
from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=4)
    ada = models.BooleanField(default=False)

    alerts = models.ManyToManyField(alerts.models.Alert)
    facilities = models.ManyToManyField(facilities.models.Facility)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"
