while True:
    adding = input('please order your favourite adding, print "quit" to end')
    if adding == 'quit':
        break
    else:
        print(adding)

active = True
while active:
    adding = input('please order your favourite adding, print "quit" to end')
    if adding == 'quit':
        active = False
        print('process end.')
    else:
        print(adding)

adding = ''
while adding != 'quit':
    adding = input('please select your favourite food, exit please print "quit".')
    if adding != 'quit':
        print(adding)
