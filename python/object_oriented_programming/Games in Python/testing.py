# seperators
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f'{total:,}')

# if else
condition = True
x = 1 if condition else 0
print(x)

# always use with

# enumarate 1
names = ['Corey', 'Steve', 'Alice', 'Bill']

for index, name in enumerate(names, start= 1):
    print(index, name)

# enumarate 2
names = ['Corey', 'Steve', 'Alice', 'Bill']
heroes = ['Superman', 'Batman', 'Wonder Woman', 'Antman']

# instead of that
for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

# do that:
for name, hero in zip(names, heroes):  #zip can unzip more than 2 lists
    print(f'{name} is actually {hero}')


# unpacking
#tuple
items = (1, 2)
print(items)

# that makes two variables
a, b = (1, 2)
print(a)
print(b)

# and that ignores one
a, _ = (1, 2)
print(a)

# and what if we want to unpack more variables?
a, b, *c = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)

#works the same why with ignoring
a, b, *_ = [1, 2, 3, 4, 5]
print(a)
print(b)
# print(c)

#more
a, b, *c, d = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)
print(d)

# classes

class Person():
    pass

person = Person()

# dynamically adding attributes to a class
person.first = "Corey"
person.last = "Schaffer"

print(person.first)
print(person.last)


#other method
class Osoba():
    pass

osoba = Osoba()
first_key = 'first'
first_val = 'Corey'

setattr(osoba, first_key, first_val) #add attribute

first = getattr(osoba, first_key) #get the attribute of class

print(osoba.first)
print(first)

# why is it important? EXAMPLE ::
# if we want to use a dictionary to add attrbutes:
person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last )

for key in person_info.keys(): # loop through the attributes using keys from a dictionary
    print(getattr(person, key))


# importing sensitive information
from getpass import getpass

username = input('Username: ')
# password = input('Password: ') # WAIT!!! the password is visible in the console!
password = getpass('Password: ')

print('Logging In...')