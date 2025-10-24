cities = {
	'Baoding':
	{'food':'lv',
	'beside the sea':'no',
	},

	'Nanjing':
	{'food':'duck',
	'beside the sea':'no',
	},

	'Weihai':
	{'food':'seafood',
	'beside the sea':'yes',
	}
}

print(cities)

for country, informations in cities.items():
	print("\n" + country + " is famous for it's " + informations['food'])
	print("is it beside the sea?" + "\n--" + informations['beside the sea'])