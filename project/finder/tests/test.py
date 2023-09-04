from django.test import SimpleTestCase
from django.urls import reverse


class FinderTests(SimpleTestCase):

    def test_filtration_of_plants(self):
        response = self.client.get(reverse("displays_plants_by_filters"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "finder/filtration_of_plants.html")
