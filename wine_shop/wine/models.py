from django.db import models


class Wine(models.Model):
    country = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    designation = models.CharField(max_length=500, blank=True)
    points = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    province = models.CharField(max_length=500, blank=True)
    region_1 = models.CharField(max_length=500,blank=True)
    region_2 = models.CharField(max_length=500,blank=True)
    variety = models.CharField(max_length=500, blank=True)
    winery = models.CharField(max_length=500, blank=True)
