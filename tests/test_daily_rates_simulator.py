from unittest import TestCase
from context import src
from src.hotel import Hotel
from src.customer import Customer
from src.daily_rates_simulator import DailyRatesSimulator
from datetime import datetime


class DailyRatesSimulatorTest(TestCase):
    def test_daily_rates_regular_week_price(self):
        hotel = Hotel("Parque das flores", 3, 110, 80, 90, 80)
        customer = Customer("Regular")
        dates = [datetime(2020, 3, 16), datetime(
            2020, 3, 17), datetime(2020, 3, 18)]

        daily_rates_simulation = DailyRatesSimulator(customer, hotel, dates)
        self.assertEqual(daily_rates_simulation.daily_rates, 330)

    def test_daily_rates_loyalty_week_price(self):
        hotel = Hotel("Parque das flores", 3, 110, 80, 90, 80)
        customer = Customer("Fidelidade")
        dates = [datetime(2020, 3, 16), datetime(
            2020, 3, 17), datetime(2020, 3, 18)]

        daily_rates_simulation = DailyRatesSimulator(customer, hotel, dates)
        self.assertEqual(daily_rates_simulation.daily_rates, 240)
    
    def test_daily_rates_regular_week_and_weekend_price(self):
        hotel = Hotel("Parque das flores", 3, 110, 80, 90, 80)
        customer = Customer("Regular")
        dates = [datetime(2020, 3, 27), datetime(
            2020, 3, 28), datetime(2020, 3, 29)]

        daily_rates_simulation = DailyRatesSimulator(customer, hotel, dates)
        self.assertEqual(daily_rates_simulation.daily_rates, 290)

    def test_daily_rates_loyalty_week_and_weekend_price(self):
        hotel = Hotel("Parque das flores", 3, 110, 80, 90, 80)
        customer = Customer("Fidelidade")
        dates = [datetime(2020, 3, 27), datetime(
            2020, 3, 28), datetime(2020, 3, 29)]

        daily_rates_simulation = DailyRatesSimulator(customer, hotel, dates)
        self.assertEqual(daily_rates_simulation.daily_rates, 240)

    def test_weekend_date(self):
        date = datetime(2021, 7, 24)

        hotel = Hotel("Parque das flores", 3, 110, 80, 90, 80)
        customer = Customer("Regular")
        dates = [datetime(2020, 3, 16), datetime(
            17, 3, 17), datetime(18, 3, 16)]

        daily_rates_simulation = DailyRatesSimulator(customer, hotel, dates)

        self.assertTrue(daily_rates_simulation.is_weekend(date))
