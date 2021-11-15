from django.db import models
from .constants import RELEASE_TAG_CHOICES

class Release(models.Model):
    ocid = models.CharField(max_length=255)
    date = models.DateTimeField()
    tag = models.CharField(max_length=255, choices=RELEASE_TAG_CHOICES) # Offer status
