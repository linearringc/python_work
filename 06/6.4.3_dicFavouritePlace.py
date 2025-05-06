favourite_place = {
	'Chenyi':['Xinzhou'],
	'Nayina':['Russian', 'Beijing', 'Xian'],
	'Jiege':['wuhan', 'tieba'],
}

for name, places in favourite_place.items():
	print("\nMy name is: " + name)
	for place in places:
		print("I love " + place)