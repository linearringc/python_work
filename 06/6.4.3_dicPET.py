puppy = {'type':'hotdog', 'mom name':'cook'}
kitten = {'type':'hello kitty', 'mom name':'cool girl'}
fish = {'type':'luyu', 'mom name':'cat'}

pets = [puppy, kitten, fish]
for pet in pets:
	print("\nMy name is " + pet['type'] + ', My mom is a ' + pet['mom name'])