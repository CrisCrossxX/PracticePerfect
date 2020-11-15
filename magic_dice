"""
makes a 6, 10, and 20 sided die to generate a random number,
(x) number of times.
"""

from random import randint

class Die:
    """class settings for die."""

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self, amount = 1):
        return [randint(1, self.sides) for i in range(amount)]

d1 = Die(10)
d2 = Die(20)

print(Die(10).roll_die(10))
print(Die(20).roll_die(10))
