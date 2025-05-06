aliens = []

for new_alien in range(30):
	new_alien = {'color':'yellow', 'points':'250'}
	aliens.append(new_alien)

for new_alien in aliens[:5]:
	print (new_alien)


print(str(len(aliens)))