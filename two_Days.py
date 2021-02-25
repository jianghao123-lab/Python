# 1_if statement
x = -1
if x < .0:
    print("'x‘ must be at least 0!")

counter = 0

# 2_while Circulation
while counter < 3:
    print('loop #%d' % (counter))
    counter += 1

# 3_for_circulation && range()function
print('I like to use the Internet for:')
for item1 in ['e-mail', 'net-surfing', 'homework', 'chat']:
    print(item1)

# 4_line feed
print('I like to use the Internet for:')
for item2 in ['e-mail', 'net-surfing', 'homework', 'chat']:
    print(item2,)
print()

# 5_Put the data together
who = 'knights'
what = 'NI!'
print('We are the', who, 'who say', what, what, what, what)
print('We are the %s who say %s' %
      (who, ((what + ' ') * 4)))


for eachNum in [0, 1, 2]:
    print(eachNum)

foo = 'abc'
for c in foo:
    print(c)

# 6_range() Built-in functions
for eachNum in range(3):
    print(eachNum)

foo = 'abc'
for i in range(len(foo)):
    print(foo[i], '(%d)' % i)

# 7_enumerate()Function
for i, ch in enumerate(foo):
    print(ch, '(%d)' % i)

# 8-list
squared = [x ** 2 for x in range(4)]
for i in squared:
    print(i)

sqdEvens = [x ** 2 for x in range(8) if not x % 2]
for i in sqdEvens:
    print(i)

# 9-open()、file()
handle = open('/Users/lenovo/PycharmProjects/test', 'r')
filename = input('Enter file name: ')
foj = open(filename, 'r')
for eachLine in foj:
    print(eachLine, foj.close())

