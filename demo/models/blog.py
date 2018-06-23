from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=256)
