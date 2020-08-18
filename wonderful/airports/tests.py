from django.test import TestCase
from airports.models import Airport

# Create your tests here.


class TestAirport(TestCase):
    def setUp(self):
        self.airport = Airport()
        self.airport.save()
