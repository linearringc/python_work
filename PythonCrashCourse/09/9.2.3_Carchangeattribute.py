class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_meter(self):
        print(str(self.odometer_reading))

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't change the odometer!")
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(88)
my_new_car.read_meter()

my_used_car = Car('VW', 'ID4', 2024)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(800)
my_used_car.read_meter()
my_used_car.increment_odometer(8000)
my_used_car.read_meter()