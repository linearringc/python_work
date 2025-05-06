from restaurant import Restaurant
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