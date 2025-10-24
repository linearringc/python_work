alien_0 = {'color':'red', 'points':'10'}
alien_1 = {'color':'black', 'points':'50'}
alien_2 = {'color':'yellow', 'points':'5'}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

aliens = []
for alien in range(30):
	new_alien = {'color':'pink', 'points':'25'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)

print('...')
print("total aliens are: " + str(len(aliens)))


