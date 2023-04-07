from django.db import models


class HousePlants(models.Model):
    name_of_plant = models.CharField(max_length=50)
    pic_of_plant = models.ImageField()
    homeland = models.CharField(max_length=100, default='')
    soil = models.CharField(max_length=100)
    min_height = models.PositiveIntegerField()
    max_height = models.PositiveIntegerField()
    flowering_time = models.CharField(max_length=50)
    leaf_color = models.CharField(max_length=100)
    light_level = models.CharField(max_length=100)
    irrigation_level = models.CharField(max_length=100)
    level_of_care = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    feeding = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    content_or_description = models.TextField()

