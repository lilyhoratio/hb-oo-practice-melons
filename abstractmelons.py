"""Refactored classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that 
    other Melon orders inherit from."""

    def __init__(self, species, qty, tax=False):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False
        if tax: self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        super().__init_(self, self.species, self.qty, tax=0.08)
        # tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        super().__init_(self, self.species, self.qty, tax=0.17)

        # tax = 0.17
        self.order_type = "international"
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        if self.qty < 10:
            return super().get_total(self) + 30
        else: return super().get_total(self)

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super().__init_(self, self.species, self.qty)

        passed_inspection = False

    def mark_inspection(passed):
        self.passed_inspection = passed