def show_magicians(magicians):
    for magician in magicians:
        msg = 'hello ' + magician
        print(msg)

magicians = ['andy', 'bowie']
show_magicians(magicians)

def make_great(magicians, the_great_magicians):
    initial_magicians = magicians.copy()
    print('This is the initial list:', initial_magicians)
    while initial_magicians:
        current_magician = 'The Great ' + initial_magicians.pop()
        the_great_magicians.append(current_magician)
    print(the_great_magicians)

magicians = ['andy', 'bowie']
the_great_magicians = []
make_great(magicians[:], the_great_magicians)
print(magicians[:])

def a(b,c):
    while b:
        d = b.pop()
        c.append(d)
        print('making:', d)
    for e in c:
        print('made:', e)


b = ['f', 'g']
c = []
a(b,c)