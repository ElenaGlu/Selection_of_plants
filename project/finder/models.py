from django.db import models


class HousePlants(models.Model):
    name_of_plant = models.CharField(max_length=50)

    homeland = models.CharField(max_length=100, default='')

    soil = models.CharField(max_length=100)

    min_height = models.PositiveIntegerField()
    max_height = models.PositiveIntegerField()

    flowering_time = models.CharField(max_length=50)

    LEAF_COLOR_CHOICES = [
        ('WH', 'White'), ('BL', 'Blue'),
        ('YE', 'Yellow'), ('GR', 'Green'),
        ('PU', 'Purple'), ('OR', 'Orange'),
        ('MO', 'Mottled'), ('PI', 'Pink'),
        ('DA', 'Dark_blue'), ('RE', 'Red'),
        ('B', 'Black')
    ]
    leaf_color = models.CharField(max_length=2, choices=LEAF_COLOR_CHOICES)

    LIGHT_LEVEL_CHOICES = [
        ('S', 'Теневыносливо'),
        ('M', 'Допустимы прямые лучи несколько часов, восточная, западная ориентация'),
        ('L', 'Западная, южная ориентация, может потребовать несколько часов прямых солнечных лучей')
    ]
    light_level = models.CharField(max_length=1, choices=LIGHT_LEVEL_CHOICES)

    IRRIGATION_LEVEL_CHOICES = [
        ('S', 'Засухоустойчиво'),
        ('M', 'Обильный полив 2-3 раза в неделю'),
        ('L', 'Нуждается в постоянно увлажненной почве (полив более 3-х раз в неделю)')
    ]
    irrigation_level = models.CharField(max_length=1, choices=IRRIGATION_LEVEL_CHOICES)

    LEVEL_OF_CARE_CHOICES = [
        ('S', 'Не нуждается в особых требованиях для роста и цветения'),
        ('M', 'В целом неприхотливо, может предъявлять особые для данного вида требования'),
        ('L', 'Требовательно в уходе')
    ]
    level_of_care = models.CharField(max_length=1, choices=LEVEL_OF_CARE_CHOICES)

    HUMIDITY_CHOICES = [
        ('S', 'Нетребовательно к влажности воздуха'),
        ('M', 'Умеренная влажность (не менее 35%, обычная уличная влажность воздуха в тени'),
        ('L', 'Высокая влажность (60% и более: тропики круглый год; типичная влажность летом в средней полосе)')
    ]
    humidity = models.CharField(max_length=1, choices=HUMIDITY_CHOICES)

    FEEDING_CHOICES = [
        ('S', 'Достаточно питательных веществ из собственной почвы или редкого удобрения'),
        ('M', 'Удобрение только в период активного роста'),
        ('L', 'Требует частого удобрения (в том числе круглый год)')
    ]
    feeding = models.CharField(max_length=1, choices=FEEDING_CHOICES)

    TEMPERATURE_CHOICES = [
        ('5', 'холодное содержание (+5 — +18°C)'),
        ('18', 'умеренно-теплое содержание (+18 — +25°C)'),
        ('22', 'теплое содержание (+22 — +27°C)'),
        ('-', 'отсутствует')
    ]
    temperature = models.CharField(max_length=2, choices=TEMPERATURE_CHOICES)

    pic_of_plant = models.ImageField()

    content_or_description = models.TextField()



