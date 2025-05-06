pizzas = ['Annies', 'domino', 'pizzahut']
for pizza in pizzas:
	#print(pizza)
	print("I love " + pizza)

print("I love all of them, CICI loves pizzahut.")

friend_pizzas = pizzas[:]
pizzas.append('101pizza')
friend_pizzas.append('Station')
print(friend_pizzas)
print(pizzas)

for pizza in pizzas:
	print("I love " + pizza + " very much!")

for friend_pizza in friend_pizzas:
	print("Dailanzi loves " + friend_pizza + " very much!")