# 1-How the input function works
message = input('Tell me something, and I will repeat it back to you')
print(message)

# 2-Write clear programs
name = input("Please enter your name:")
print("Hello,"+name+"!")

prompt = "if you tell us who you are, we can persinalize the messages you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\nHello,"+name+"!")

# 3-Use int() to get numeric input
age = input("How old are you?")
age = int(age)
age >= 18

height = input("How tall are you, in inches?")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou're be albe to ride when you're a little older.")

# 4-Evaluate modulo operators
4 % 3

5 % 3

6 % 3

number = input("Enter a number,and I'll tell you if it's even or add:")
number = int(number)
if number % 2 == 0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd")

    # car rental
car = input("what kind of car do you want to rent:")
print("\nLetmeseeifIcan find you a "+str(car))

# The restaurant reservation
seat = input("Ask the user how many people are eating:")
seat = int(seat)
if seat >= 8:
    print("No seat!")
else:
    print("Have seat!")

    # Integer multiples of 10
Integer = input("Please enter a number:")
Integer = int(Integer)
if Integer % 10 == 0:
    print("yes")
else:
    print("No")

# 5-Use while range
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 6-Let users choose when to lunch
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit to end the program.'"
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# 7-Use sign
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program,"
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# 8-Use break to push out the loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd have to go to San Francisco!")

# 9-Use continue in the loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 10-Avoid infintite loops
x = 1
while x <= 5:
    print(x)
    x += 1

    # The loop will run indefinitely
x = 1
while x <= 5:
    print(x)

    # Pizza toppings
prompt = " The user enters alist of pizza ingredients "
while True:
    user = input(prompt)
    if user == 'quit':
        break
    else:
        prompt = "We add it to our pizzas "

#   cinema ticket
prompt = "Please tell me your age "
while True:
    age = input(prompt)
    if age != 'quit':
        if int(age) <= 3:
            print("The audience for free")
        elif int(age) <= 12:
            print("The audience ten yuan")
        elif int(age) > 12:
            print("The audience fifth yuan")
    else:
        break

# 11-Use a while loop to process lists and dictionaries
    # First,create a list of users to validate
unconfiremed_users = ['alice', 'brian', 'candace']
# And an empty list to store authenticated users
confirmed_users = []
    # Validate each user until there are no unauthenticated users
while unconfiremed_users:
    current_user = unconfiremed_users.pop()
    print("Verifying user:" + current_user.title())
    # Move each authenticated list to the list of authenticated users
    confirmed_users.append(current_user)
    # Displays all authenticated users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
    # Set a flag indicating whether the investigation should continue
polling_active = True
while polling_active:
    # PROMPT FOR THE RESPONDENT'S NAME AND ANSWER
    name = input("\nwhat is your name? ")
    response = input("which mountain would you like to climb someday? ")
    # Store the answer paper in a dictionary
    responses[name] = response
    # See if anyone else wants to participate in the survey
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False
    # The survey is over and the results are shown
print("\n---Poll Results----")
for name, response in responses.items():
    print(name + "would like to climb"+response+".")

sandwich_orders = ['蛋黄三明治', '奶酪火腿三明治', '三文鱼三明治']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
print('finished_sandwich')
for sandwich in finished_sandwiches:
    print('I made your tuna sandwich')
    print(sandwich)

sandwich_orders = ['五香牛肉', '蛋黄三明治', '奶酪火腿三明治', '三文鱼三明治']
print("五香牛肉卖完了")
while "五香牛肉" in sandwich_orders:
    sandwich_orders.remove('五香牛肉')
for sandwich in sandwich_orders:
    print(sandwich)

name_place = {}
print("问卷调查，任何时候，打‘quit'退出")
while True:
    name = input("你的名字")
    if name == 'quit':
        break
    else:
        place = input("你最想去的地方")
