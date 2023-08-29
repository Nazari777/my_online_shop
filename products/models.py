from django.db import models

class Member(models.Model):
  name = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
  stock = models.FloatField()
  image_url = models.CharField(max_length=2083)