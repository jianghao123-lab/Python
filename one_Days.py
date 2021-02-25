print("Hello world")

myString = 'hello world!'
print(myString)

# 3- String conversion
print("%s is number %d!" % ("python", 1))

# 4-redirect
import sys
sys.stderr, 'Fatal error: invalid input'

# 5-multiplying operator   --**
print(-4*2+3**2)

# 6-compare operator
2<4 and 2==4
2>4 or 2<4
not 6.2 <=6

# 7-Variables and assignments
counter = 0
miles = 1000.0
name = 'Bob'
counter = counter + 1
kilometers = 1.609 * miles
print('%f miles is the same as %f km' % (miles, kilometers))

# 8-string
pyster = 'python'
iscool = 'is cool!'
pyster + " " + iscool

# 9-Slicing operation
aList = [1,2,3,4]
aList[:2]
aList[3:]

# 10-Array
aTuple = ('robots', 77, 93, 'trys')
aTuple
aTuple[:3]

# 11-Key-value
aDict = {'host' : 'earth'}
aDict['port'] = 80
aDict

for key in aDict:
    print(key, aDict[key])

# 12-The directional output
print('Fatal error：invalid input', file = sys.stderr)

# 13-input function
user =input ('Enter login name: ')
print('You login is:', user)

# 14-Assign a number
n = 1
n *= 10
n