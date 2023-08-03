from django.test import TestCase
from django.urls import reverse
from django.test import Client


class FinderTests(TestCase):

    def test_filtration_of_plants(self):
        c = Client()
        response = c.get(reverse("displays_plants_by_filters"), )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "finder/filtration_of_plants.html")
