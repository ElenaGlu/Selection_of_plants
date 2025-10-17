from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)


class Care(models.Model):
    level_of_care = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.level_of_care


class Light(models.Model):
    light_level = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.light_level


class Irrigation(models.Model):
    irrigation_level = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.irrigation_level


class Temperature(models.Model):
    temperature_level = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.temperature_level


class Humidity(models.Model):
    humidity_level = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.humidity_level


class Feeding(models.Model):
    feeding_level = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.feeding_level


class Soil(models.Model):
    soil = models.CharField(max_length=300, null=True, blank=True)


class FloweringTime(models.Model):
    time = models.CharField(max_length=300, null=True, blank=True)


class LeafColor(models.Model):
    color = models.CharField(max_length=500, null=True, blank=True)


class Plant(models.Model):
    full_name = models.CharField(max_length=300, null=True, blank=True)
    short_name = models.CharField(max_length=300, null=True, blank=True)
    min_height = models.PositiveIntegerField(null=True, blank=True)
    max_height = models.PositiveIntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image_link = models.CharField(max_length=300, null=True, blank=True)

    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    care = models.ForeignKey(Care, on_delete=models.CASCADE)
    light = models.ForeignKey(Light, on_delete=models.CASCADE)
    irrigation = models.ForeignKey(Irrigation, on_delete=models.CASCADE)
    temperature = models.ForeignKey(Temperature, on_delete=models.CASCADE)
    humidity = models.ForeignKey(Humidity, on_delete=models.CASCADE)
    feeding = models.ForeignKey(Feeding, on_delete=models.CASCADE)
    soil = models.ForeignKey(Soil, on_delete=models.CASCADE)
    flowering_time = models.ForeignKey(FloweringTime, on_delete=models.CASCADE)
    leaf_color = models.ForeignKey(LeafColor, on_delete=models.CASCADE)
