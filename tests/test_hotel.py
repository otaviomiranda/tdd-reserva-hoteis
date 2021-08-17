from unittest import TestCase
from context import src
from src.hotel import Hotel


class HotelTest(TestCase):
    def test_name(self):
        hotel = Hotel("Parque das flores", 3, 110, 80, 90, 80)
        self.assertEqual(hotel.name, "Parque das flores")

    def test_rating(self):
        hotel = Hotel("Parque das flores", 3, 110, 80, 90, 80)
        self.assertEqual(hotel.rating, 3)

    def test_rating_bigger_than_5(self):
        with self.assertRaises(Exception) as context:
            Hotel("Parque das flores", 6, 110, 80, 90, 80)

        self.assertTrue(
            "The rating value must be between 1 and 5" in str(context.exception))

    def test_rating_smaller_than_1(self):
        with self.assertRaises(Exception) as context:
            Hotel("Parque das flores", 0, 110, 80, 90, 80)

        self.assertTrue(
            "The rating value must be between 1 and 5" in str(context.exception))
    
    def test_regular_week_rate_zero(self):
        with self.assertRaises(Exception) as context:
            Hotel("Parque das flores", 3, 0, 80, 90, 80)

        self.assertTrue(
            "The 'regular_week_rate value' must be bigger than 0" in str(context.exception))