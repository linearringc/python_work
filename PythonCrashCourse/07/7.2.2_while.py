prompt = 'I will repeat what you say,'
prompt += '\nUntil you print "quit".'

message = ''
while message != 'quit':
    message = input(prompt)
    #print(message)
    if message != 'quit':
        print(message)


message = ''
while message != 'quit':
    message = input('\nI will repeat what you say until you print "quit".')
    if message != 'quit':
        print(message)