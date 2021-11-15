from django.db import models

# Create your models here.
class music_data(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, blank=True)

def __str__(self):
    return self.title