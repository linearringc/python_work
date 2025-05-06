favourite_numbers = {'Ada':6, 'Bob':4, 'Cici':6}
for na, me in favourite_numbers.items():
	print(na, me)

for na in favourite_numbers.keys():
	print(na)

for na in favourite_numbers.keys():
	if na =='Ada':
		print("ada's favourite number is 6")
	else:
		print('your favourite number is 4 or 8')

friends = ['Ada', 'Cici']
for na in favourite_numbers:
	print(na)
	if na in friends:
		print(na + str(favourite_numbers[na]))

print(favourite_numbers.keys())

for na in favourite_numbers.values():
	print(na)

for number in set(favourite_numbers.values()):
	print(number)

for number in sorted(favourite_numbers.values()):
	print(number)

guys = ['Ada', 'Laoba', 'Bob']
for guy in guys:
	print(guy)
	if guy in favourite_numbers.keys():
		print("thank you for your involve " + guy)
	else:
		print('Please register')