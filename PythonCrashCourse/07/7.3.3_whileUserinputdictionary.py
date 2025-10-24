responses = {}
active = True
while active:
    name = input('\nPlease tell me your name:')
    age = input('Please tell me your age:')
    age = int(age)

    responses[name] = age
    answer = input('Do you want to come here(yes/no)?')
    active = False


print(responses)

