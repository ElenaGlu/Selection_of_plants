from django.test import TestCase
from django.urls import reverse


class FiltersTests(TestCase):
    """
    Requests a html page and checks its status code and the correctness of the template.
    """
    def test_filtration_of_plants(self):
        response = self.client.get(reverse("displays_plants_by_filters"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "finder/filtration_of_plants.html")
