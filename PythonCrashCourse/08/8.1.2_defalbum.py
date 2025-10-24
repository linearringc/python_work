def make_album (singer, album):
    full_album = 'I am ' + singer + ' My album is ' + album
    return full_album
while True:
    singers = input('who is your favourite singer:')
    albums =input('which is his/her favourite album:')
    answer = input('print "quit" to exit.')
    print(make_album(album = singers, singer = albums))
    if answer == 'quit':
        break
