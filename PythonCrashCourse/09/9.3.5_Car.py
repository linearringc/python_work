class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size ==85:
            range = 270
        message = 'This car can go ' + str(range)
        print(message)

    def upgrade_battery(self):
        """检查电瓶容量"""
        if self.battery_size != 85:
            self.battery_size = 85
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('Tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

car = ElectricCar('VW', 'ID4', 2024)
car.battery.upgrade_battery()