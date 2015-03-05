import datetime
from django.db import models

# Create your models here.
class Alert(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    published = models.BooleanField(default=False)
    recurring = models.BooleanField(default=False)
    publish_date = models.DateTimeField()
    publish_end_data = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "Alert"
        verbose_name_plural = "Alerts"

    def save(self, *args, **kwargs):
        if self.published and not self.published_date:
            self.published_date = datetime.now()

        super(Alert, self).save(*args, **kwargs)

