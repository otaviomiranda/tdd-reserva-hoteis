from src.customer import Customer
from src.hotel import Hotel
from datetime import datetime


class DailyRatesSimulator:
    def __init__(self, customer: Customer, hotel: Hotel, dates: list) -> None:
        self.customer = customer
        self.hotel = hotel
        self.daily_rates = dates

    @property
    def customer(self) -> Customer:
        return self._customer

    @customer.setter
    def customer(self, customer: Customer) -> None:
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise("The 'customer' value must be of Customer type")

    @property
    def hotel(self) -> Hotel:
        return self._hotel

    @hotel.setter
    def hotel(self, hotel: Hotel) -> None:
        if isinstance(hotel, Hotel):
            self._hotel = hotel
        else:
            raise("The 'hotel' value must be of Hotel type")

    @property
    def daily_rates(self) -> float:
        return self._daily_rates

    @daily_rates.setter
    def daily_rates(self, dates: list) -> None:
        total = 0

        for date in dates:
            if self.is_weekend(date):
                if self.customer.is_loyalty_customer:
                    total += self.hotel.loyalty_weekend_rate
                else:
                    total += self.hotel.regular_weekend_rate
            else:
                if self.customer.is_loyalty_customer:
                    total += self.hotel.loyalty_week_rate
                else:
                    total += self.hotel.regular_week_rate
        
        self._daily_rates = total


    def is_weekend(seld, date: datetime) -> bool:
        if date.weekday() < 5:
            return False
        else:
            return True
