from random import randint

class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        print(f"number is {result}")

six_sided_die = Die()

for _ in range(10):
    six_sided_die.roll_die()