from django.db import models


class Uri(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
