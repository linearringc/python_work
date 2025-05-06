def make_car(vendor, type, **info):
    car_info = {}
    car_info['vendor'] = vendor
    car_info['type'] = type
    for key, value in info.items():
        car_info[key] = value
    return car_info

car = make_car('audi', 'A4', color='blue', two_package=True)
print(car)