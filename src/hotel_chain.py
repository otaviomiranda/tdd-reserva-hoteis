from src.customer import Customer
from src.hotel import Hotel
from src.daily_rates_simulator import DailyRatesSimulator


class HotelChain:
    def __init__(self) -> None:
        self.hotels = []

    def add_hotel(self, name: str, rating: int, regular_week_rate: float, loyalty_week_rate: float,
                  regular_weekend_rate: float, loyalty_weekend_rate: float) -> None:

        hotel = Hotel(name, rating, regular_week_rate, loyalty_week_rate,
                      regular_weekend_rate, loyalty_weekend_rate)

        self.hotels.append(hotel)

    def get_cheaper_hotel(self, customer: Customer, dates: list):
        daily_rates_hotels_simulation = []
        for hotel in self.hotels:
            daily_rates = DailyRatesSimulator(customer, hotel, dates)
            daily_rates_hotels_simulation.append(daily_rates)

        cheaper_hotel = sorted(daily_rates_hotels_simulation, key=lambda k: (
            k.daily_rates, -k.hotel.rating))[0]

        return cheaper_hotel.hotel.name
