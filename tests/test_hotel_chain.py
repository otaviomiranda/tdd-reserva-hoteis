from unittest import TestCase
from context import src
from src.hotel_chain import HotelChain
from src.customer import Customer
from datetime import datetime

class HotelChainTest(TestCase):
    def test_create_hotel(self):
        hotel_chain = HotelChain()
        hotel_chain.add_hotel("Parque das flores", 3, 110, 80, 90, 80)

        length = len(hotel_chain.hotels)

        self.assertEqual(
            hotel_chain.hotels[length - 1].name, "Parque das flores")

    def test_cheaper_hotel(self):
        hotel_chain = HotelChain()

        hotel_chain.add_hotel("Parque das flores", 3, 110, 80, 90, 80)
        hotel_chain.add_hotel("Jardim Botânico", 4, 160, 110, 60, 50)
        hotel_chain.add_hotel("Mar Atlântico", 5, 220, 100, 150, 40)

        customer = Customer("Fidelidade")
        dates = [datetime(2020, 3, 26), datetime(2020, 3, 27), datetime(2020, 3, 28)]

        cheaper_hotel = hotel_chain.get_cheaper_hotel(customer, dates)

        self.assertEqual(cheaper_hotel, "Mar Atlântico")
