from django.db import models
from django.contrib.auth.models import User


class Tips(models.Model):
    tipsid = models.IntegerField(blank=True, null=True)
    photo = models.URLField(max_length=256, blank=True)
    tips = models.CharField(default="", max_length=500, blank=True, null=True)

