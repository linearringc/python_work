def make_pizza(size, *toppings):
    print("\nyou've ordered a " + str(size) + '-inch pizza with following toppings:')
    for topping in toppings:
        print('-' + topping)
