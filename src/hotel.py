class Hotel:

    def __init__(self, name: str, rating: int, regular_week_rate: float, loyalty_week_rate: float,
                 regular_weekend_rate: float, loyalty_weekend_rate: float) -> None:
        self.name = name
        self.rating = rating
        self.regular_week_rate = regular_week_rate
        self.loyalty_week_rate = loyalty_week_rate
        self.regular_weekend_rate = regular_weekend_rate
        self.loyalty_weekend_rate = loyalty_weekend_rate

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def rating(self) -> int:
        return self._rating

    @rating.setter
    def rating(self, rating: int) -> None:
        if rating in [1, 2, 3, 4, 5]:
            self._rating = rating
        else:
            raise Exception("The rating value must be between 1 and 5")

    @property
    def regular_week_rate(self) -> float:
        return self._regular_week_rate

    @regular_week_rate.setter
    def regular_week_rate(self, regular_week_rate: float) -> None:
        if regular_week_rate > 0:
            self._regular_week_rate = regular_week_rate
        else:
            raise Exception(
                "The 'regular_week_rate value' must be bigger than 0")

    @property
    def loyalty_week_rate(self) -> float:
        return self._loyalty_week_rate

    @loyalty_week_rate.setter
    def loyalty_week_rate(self, loyalty_week_rate: float) -> None:
        if loyalty_week_rate > 0:
            self._loyalty_week_rate = loyalty_week_rate
        else:
            raise Exception(
                "The loyalty_week_rate value must be bigger than 0")

    @property
    def regular_weekend_rate(self) -> float:
        return self._regular_weekend_rate

    @regular_weekend_rate.setter
    def regular_weekend_rate(self, regular_weekend_rate: float) -> None:
        if regular_weekend_rate > 0:
            self._regular_weekend_rate = regular_weekend_rate
        else:
            raise Exception(
                "The regular_weekend_rate value must be bigger than 0")

    @property
    def loyalty_weekend_rate(self) -> float:
        return self._loyalty_weekend_rate

    @loyalty_weekend_rate.setter
    def loyalty_weekend_rate(self, loyalty_weekend_rate: float) -> None:
        if loyalty_weekend_rate > 0:
            self._loyalty_weekend_rate = loyalty_weekend_rate
        else:
            raise Exception(
                "The loyalty_weekend_rate value must be bigger than 0")

    