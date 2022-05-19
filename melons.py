"""Classes for melon orders."""

class AbstractMelonOrder:

    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == 'Chrstimas':
            base_price = base_price * 1.5        
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True     

class GovernmentMelonOrder(AbstractMelonOrder):
    """Government Melon Orders."""
    tax = 0
    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self):
        """Record the fact than an order has been passed."""

        self.passed_inspection = True     

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

    
    def get_total(self):
        """Calculate price, including tax."""
        sub_total = super().get_total()
        if self.qty < 10:
            sub_total = sub_total + 3

        return sub_total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
