from unittest import TestCase
from context import src
from src import main, prepare_entry


class InitTest(TestCase):
    def test_prepate_entry_customer_type(self):
        customer_type, _ = prepare_entry(
            "Regular: 20Mar2020(fri), 21Mar2020(sat), 22Mar2020(sun)")
        self.assertEqual(customer_type, "Regular")

    def test_main_regular_week_entry(self):
        cheaper_hotel_name = main(
            "Regular: 16Mar2020(mon), 17Mar2020(tues), 18Mar2020(wed)")
        self.assertEqual(cheaper_hotel_name, "Parque das flores")

    def test_main_regular_week_and_weekend_entry(self):
        cheaper_hotel_name = main(
            "Regular: 20Mar2020(fri), 21Mar2020(sat), 22Mar2020(sun)")
        self.assertEqual(cheaper_hotel_name, "Jardim Botânico")

    def test_main_loyalty_week_and_weekend_entry(self):
        cheaper_hotel_name = main(
            "Fidelidade: 26Mar2020(thur), 27Mar2020(fri), 28Mar2020(sat)")
        self.assertEqual(cheaper_hotel_name, "Mar Atlântico")