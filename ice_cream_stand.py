class Restaurant:
    """describes food and the time it is open."""

    def __init__(self, name, type):
        """initialize name and type attributes."""
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"Restaurant {self.name} is now open.")
        print(f"They serve {self.type} food.")

my_restaurant = Restaurant('deleon', 'mexiasian')

class IceCreamStand(Restaurant):
    """describes the flavors of ice-cream."""
    def __init__(self, name, type, flavors):
    """initialize flavors."""
        super().__init__(name, type)
        self.flavors = flavors

    def describe_flavor(self):
        print(f"{self.name} is now serving {self.type}!")
        print(f"today's selection includes: {self.flavors.title()}.")

my_flavors = IceCreamStand('deleon', 'ice cream',
                           '[vanilla, dark-chocolate, cookie-dough]'
                           )
my_flavors.describe_flavor()
