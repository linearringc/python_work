age = input('please tell me your age, I will tell you how much is the ticket.')
age = int(age)
if age < 3:
    print('0 dollar')
elif age <= 12:
    print('10 dollar')
elif age > 12:
    print('15 dollar')


