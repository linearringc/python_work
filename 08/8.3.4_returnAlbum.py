def make_album(singer, album):
    full_album = singer + ' loves ' + album
    return full_album

while True:
    singer = input('Please tell me your favourite singer:')
    album = input('Please tell me her/his best album:')
    answer = input('Thank you for your time, type in "quit" to exit.')

    print(make_album(singer, album))

    if answer == 'quit':
        break



#Nayina = make_album('Nayina', 'Sheinenggeiwoai')
#Matt_lv = make_album('Matt lv', 'gogogo')
#Chenyi = make_album('Chenyi', 'Xinzhoupop', '12')
#print(Nayina)
#print(Matt_lv)
#print(Chenyi)
