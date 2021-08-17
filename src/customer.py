class Customer:
    def __init__(self, loyalty_customer_type: str) -> None:
        self.is_loyalty_customer = loyalty_customer_type

    @property
    def is_loyalty_customer(self) -> bool:
        return self._is_loyalty_customer

    @is_loyalty_customer.setter
    def is_loyalty_customer(self, loyalty_customer_type: str) -> None:
        if loyalty_customer_type == "Regular":
            self._is_loyalty_customer = False
        elif loyalty_customer_type == "Fidelidade":
            self._is_loyalty_customer = True
        else:
            raise Exception(
                "The 'loyalty_customer_type' value must be 'Regular' or 'Fidelidade'")
