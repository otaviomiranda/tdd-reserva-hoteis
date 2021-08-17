from unittest import TestCase
from context import src
from src.customer import Customer


class CustomerTest(TestCase):
    def test_client_loyalty(self):
        customer = Customer("Fidelidade")
        self.assertTrue(customer.is_loyalty_customer)

    def test_client_regular(self):
        customer = Customer("Regular")
        self.assertFalse(customer.is_loyalty_customer)

    def test_client_type(self):
        with self.assertRaises(Exception) as context:
            Customer("aaa")

        self.assertTrue("The 'loyalty_customer_type' value must be 'Regular' or 'Fidelidade'" in str(
            context.exception))
