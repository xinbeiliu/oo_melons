"""Classes for melon orders."""
from random import randint

class AbstractMelonOrder():
    """Any melon order"""

    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == 'Christmas melon':
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):

        base_price = randint(5, 9)

        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):

        total = super().get_total()

        if self.qty < 10:
            total += 3

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """class for melons with specail government tax"""
    passed_inspection = None
    tax = 0

    def mark_inspection(self, passed):
        self.passed_inspection = passed
