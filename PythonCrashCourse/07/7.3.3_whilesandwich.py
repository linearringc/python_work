sandwich_orders = ['pastrami sandwich','pastrami sandwich', 'egg sandwich', 'pastrami sandwich', 'tomato sandwich', 'chicken sandwich']
finished_sandwiches = []
print('pastrami sandwich has been sold out.')

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

print(sandwich_orders)

while sandwich_orders:
    current_order = sandwich_orders.pop()
    finished_sandwiches.append(current_order)
    print('I made your ' + current_order)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)