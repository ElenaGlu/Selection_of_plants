from django.db import models


class HousePlants(models.Model):
    name_of_plant = models.CharField(max_length=500)
    homeland = models.CharField(max_length=500, null=True)
    soil = models.CharField(max_length=500, null=True)
    min_height = models.PositiveIntegerField(null=True)
    max_height = models.PositiveIntegerField(null=True)
    flowering_time = models.CharField(max_length=500, null=True)
    leaf_color = models.CharField(max_length=500, null=True)
    light_level = models.CharField(max_length=500, null=True)
    irrigation_level = models.CharField(max_length=500, null=True)
    level_of_care = models.CharField(max_length=500, null=True)
    humidity = models.CharField(max_length=500, null=True)
    feeding = models.CharField(max_length=500, null=True)
    temperature = models.CharField(max_length=500, null=True)
    content_or_description = models.TextField(null=True)
    pic_of_plant = models.CharField(max_length=500, null=True)

