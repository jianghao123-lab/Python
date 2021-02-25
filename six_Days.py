# 1-if_statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# 2-and
age_0 = 22
age_1 = 18
age_0 > 21 and age_1 > 21


# 3-or
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

# 4-in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

# 5-Boolean
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')    #true
print("Is car == 'audi'? I predict True.")
print(car =="audi")     #false

# 6-if_else
age = 17
if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote")
    print("please register to vote as soon as you turn 18")

# 7-if_elif_else
age = 12
if age < 4:
    print("You admission cost is $0.")
elif age<18:
    print("You admission cost is $5")
else:
    print("You admission cost is $10")

# 8-for
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
     print("Sorry, we are out of green peppers right now.")
else:
    print("Adding " + requested_topping + ".")