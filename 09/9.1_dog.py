from encodings.punycode import selective_find


class Dog():
    def __init__(self, name, age):
        '''初始化属性name& age'''
        self.name = name
        self. age = age

    def sit(self):
        print(self.name + ' is sitting.')

    def rollover(self):
        print(self.name + ' is rolling.')

my_dog = Dog('Chenyi', 6)
your_dog = Dog('Nayina', 70)
print("my dog's name is " + my_dog.name)
print("my dog's age is " + str(my_dog.age))
my_dog.sit()
my_dog.rollover()

print("\nmy dog's name is " + your_dog.name)
print("my dog's age is " + str(your_dog.age))
your_dog.sit()
your_dog.rollover()



