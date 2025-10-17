# from django.core.management.base import BaseCommand
# from finder.models import HousePlants, Plant, Region, Care, Light, Irrigation, Temperature, Humidity, Feeding, Soil, \
#     FloweringTime, LeafColor
#
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         for old in HousePlants.objects.all():
#             region_obj, _ = Region.objects.get_or_create(name=old.homeland)
#             care_obj, _ = Care.objects.get_or_create(level_of_care=old.level_of_care)
#             light_obj, _ = Light.objects.get_or_create(light_level=old.light_level)
#             irrigation_obj, _ = Irrigation.objects.get_or_create(irrigation_level=old.irrigation_level)
#             temp_obj, _ = Temperature.objects.get_or_create(temperature_level=old.temperature)
#             humidity_obj, _ = Humidity.objects.get_or_create(humidity_level=old.humidity)
#             feeding_obj, _ = Feeding.objects.get_or_create(feeding_level=old.feeding)
#             soil_obj, _ = Soil.objects.get_or_create(soil=old.soil)
#             flowering_obj, _ = FloweringTime.objects.get_or_create(time=old.flowering_time)
#             leaf_color_obj, _ = LeafColor.objects.get_or_create(color=old.leaf_color)
#
#             Plant.objects.create(
#                 full_name=old.name_of_plant,
#                 short_name=old.short_name,
#                 min_height=old.min_height,
#                 max_height=old.max_height,
#                 content=old.content_or_description,
#                 image_link=old.pic_of_plant,
#                 region=region_obj,
#                 care=care_obj,
#                 light=light_obj,
#                 irrigation=irrigation_obj,
#                 temperature=temp_obj,
#                 humidity=humidity_obj,
#                 feeding=feeding_obj,
#                 soil=soil_obj,
#                 flowering_time=flowering_obj,
#                 leaf_color=leaf_color_obj,
#             )
