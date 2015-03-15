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
    published = models.BooleanField(default=False)
    owner = models.CharField(max_length=70, null=True)
    owner_link = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=10, null=True)

    alerts = models.ManyToManyField(alerts.models.Alert)
    facilities = models.ManyToManyField(facilities.models.Facility)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            name = re.sub(' ', '_', self.name)
            self.slug = name[0:50]

            temp = Site.objects.filter(slug=self.slug)
            if len(temp) > 0:
                self.slug = self.slug[0:49] + '0'

        super(Site, self).save(*args, **kwargs)

    def published(self):
        published = True

    def unpublished(self):
        published = False


