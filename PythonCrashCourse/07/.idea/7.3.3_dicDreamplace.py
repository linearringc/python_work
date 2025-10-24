response = {}
active = True
while active:
    name = input('please tell me your name:')
    place = input('please tell me where you want to go:')
    response[name] = place

    answer = input('do you want to go there with us?(yes/no):')
    if answer.lower()  == 'yes':
        contact_number = input('please tell me your phone number, we will contact with you:')
        response[answer] = contact_number
        active = False

    elif answer.lower() == 'no':
        print('thank you for your time, hope you a happy trip.')
        active = False

print('thank you for your time, have a good trip!')
print(response)