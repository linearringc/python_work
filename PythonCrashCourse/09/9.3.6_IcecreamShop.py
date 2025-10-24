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

class IcecreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['apple', 'banana', 'pineapple']

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

Annie = IcecreamStand('Annie', 'Italian')
Annie.describe_restaurant()
Annie.show_flavors()