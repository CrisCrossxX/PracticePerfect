class Car:
    """a simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 95400
    def get_descriptive_name(self):
        """return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_best_car = Car('mazda', 'mx5', 1992)
print(my_best_car.get_descriptive_name())
my_best_car.read_odometer()