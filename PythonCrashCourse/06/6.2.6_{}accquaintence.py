accquaintence = {'first_name':'Chen', 'Last_name':'yi', 'age':'22', 'city':'Xinzhou'}
print(accquaintence['first_name'])
print(accquaintence['Last_name'])
print(accquaintence['age'])
print(accquaintence['city'])

favourite_number = {'Chenyi':'985211', 'Laoba':'8', 'Nayina':'2', 'guy':'616','Kier':'9'}
print("Chenyi's favourite number is " + favourite_number['Chenyi'])

Light = {'first_name':'Light', 'Last_name':'opposit', 'age':'16', 'city':'tokyo'}
Youmei = {'first_name':'youmei', 'Last_name':'night', 'age':'17', 'city':'tokyo'}

people = [accquaintence, Light, Youmei]
print(people)

for guy in people:
	print('\n' + guy['first_name'] + guy['Last_name'] + "'s age is " + guy['age'] + ',\nliving in ' + guy['city'])