# 1_for_Circulation
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title()+", that was a great trick")

magician = ['alice', 'david', 'carlina']
for magician in magicians:
    print(magician.title() + ", that was a great trick")
    print("I can't wait to see your next trick," + magician.title() + ".\n")

# 2_for_Circulation_Fruit
fruit = ['apple', 'banana', 'pear']
for fruits in fruit:
    print(fruits)
    print("I like this fruit")
print("I really love print")

# 3-use_Function_range()
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)
odd_numbers = list(range(2, 11, 1))
print(odd_numbers)

squars = []
for value in range(1, 11):
    squars. append(value ** 2)
print(squars)

# 4_numbers_List
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

# 5_list_Comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squars)

# 6_slice_up
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 7-Copy the list
my_foods = ['pizza', 'falafel', 'carrot cake']
firend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("firend favorite foods are")
print(firend_foods)

# 8-tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car== "bmw":
        print(car.upper())
    else:
        print(car.title())