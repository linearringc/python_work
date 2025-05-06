request_toppings = ['fish', 'onion', 'green peper']
requested_toppings = ['mushroom', 'green peper', 'onion']

for requested_topping in requested_toppings:
	if requested_topping in request_toppings:
		print(requested_topping + 'is available')
	else:
		print("we don't have " + requested_topping)