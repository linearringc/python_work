alien_color = 'yellow'
#if alien_color == "green":
	#print("Congratulations! you gain 5 points.")

#if alien_color == 'green':
	#print('Congratulations! you gain 5 points.')
#if alien_color != 'green':
	#print('Congratulations! you gain 10 points.')

#if alien_color == 'green':
	#print('Congratulations! you gain 5 points.')
#else:
	#print('Congratulations! you gain 10 points.')

if alien_color == 'green':
	print('Congratulations! you gain 5 points.')
elif alien_color == 'yellow':
	print('Congratulations! you gain 10 points.')
else:
	print('Congratulations! you gain 20 points.')

if alien_color == 'green':
	dot = '5'
elif alien_color == 'yellow':
	dot = '10'
else :
	dot = '20'

print('Congratulations! you gain ' + dot + ' points.')