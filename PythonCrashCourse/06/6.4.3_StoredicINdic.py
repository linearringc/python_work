users = {
	'TOM':{
	'age':30,
	'sex':'male',
	'height':'165',
	},
	'BOB':{
	'age':99,
	'sex':'female',
	'height':'199',
	}
}

for user_name, info in users.items():
	print(user_name)
	age = info['age']
	print(age)

