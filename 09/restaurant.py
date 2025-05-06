class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        '''初始化restaurant_name,和cuisine_type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_severed = 8

    def describe_restaurant(self):
        print("\nour restaurants' name is: " + self.restaurant_name)
        print("our restaurants' cuisine type is: " + self.cuisine_type)

    def open_restaurant(self):
        print('our restaurant is opening.')

    def read_number_severed(self):
        print('We have severed ' + str(self.number_severed) + ' customers')

    def set_number_served(self, customer_number):
        self.number_severed = customer_number

    def add_number_served(self, new_customers):
        self.number_severed += new_customers


restaurant1 = Restaurant('Annie', 'France cuisine')
restaurant2 = Restaurant('Pips', 'American cuisine')
restaurant3 = Restaurant('zufu', 'Chinese cuisine')

restaurant1.set_number_served(88)
restaurant1.add_number_served(100)

restaurant1.read_number_severed()
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)