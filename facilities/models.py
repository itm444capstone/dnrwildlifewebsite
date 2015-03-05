from django.db import models

# Create your models here.
class Facility(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="icons/")

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
