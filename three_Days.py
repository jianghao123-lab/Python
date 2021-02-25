# 1_define Function

def addme2me(x):
    return x + x


addme2me(5)


# 2


def foo(debug=True):
    if debug:
        print("in debug mode")
        print('done')


foo()
foo(False)


# 3_class


class FooClass(object):
    version = 0.1  # class （date）attribute

    def __init__(self, nm='John Doe'):
        self.name = nm
        print('Created a class instance for', nm)

    def showname(self):
        print('Your name is', self.name)
        print('My name is', self.__class__.__name__)

    def showver(self):
        print(self.version)

    def addme2me(self, x):
        return x + x


fool = FooClass()
fool.showname()
fool.showver()
print(fool.addme2me(5))
