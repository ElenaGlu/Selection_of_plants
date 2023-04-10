from django.db import models


class HousePlants(models.Model):
    name_of_plant = models.CharField(max_length=50)
    pic_of_plant = models.ImageField()
    homeland = models.CharField(max_length=200, default='')
    soil = models.CharField(max_length=200)
    min_height = models.PositiveIntegerField()
    max_height = models.PositiveIntegerField()
    flowering_time = models.CharField(max_length=200)
    leaf_color = models.CharField(max_length=200)
    light_level = models.CharField(max_length=200)
    irrigation_level = models.CharField(max_length=200, null=True)
    level_of_care = models.CharField(max_length=200, null=True)
    humidity = models.CharField(max_length=200, null=True)
    feeding = models.CharField(max_length=200, null=True)
    temperature = models.CharField(max_length=200, null=True)
    content_or_description = models.TextField()

