# 1_define function
def greet_user():
    """显示简单的问候语"""
    print("Hello")


greet_user()


def greet_user(username):
    """显示简单的问候语"""
    print("Hello,"+username.title()+"!")


greet_user('Jesse')


# Test_message
def display_message():
    print("function")


display_message()


# Test_like's book
def favorite_book(book):
    print("One of my favorite books is "+book.title())


favorite_book('alice in wonderland')

# 2_Pass arguments
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a"+animal_type+".")
    print("My"+animal_type+"'s name is"+pet_name.title()+".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

def describe_pet(animal_type, pet_name):
    print("\nI have a"+animal_type+".")
    print("My"+animal_type+"'s name is"+pet_name.title()+".")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a"+animal_type+".")
    print("My"+animal_type+"'s name is"+pet_name.title()+".")
describe_pet(pet_name='willie')

describe_pet("while")

def describe_prt(animal_type, pet_name):
    print("\nI have a"+animal_type+".")
    print("My"+animal_type+"'s name is"+pet_name.title()+".")
describe_pet()

# 3-returned Value
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name +" "+ last_name
    return full_name.title()
musician =get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + " " +middle_name+" "+last_name
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person =  {'first':first_name, 'last':last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    """返回一个字典 ，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
# 这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First_name:")
    if f_name == 'q':
        break;
    l_name = input("Last name:")
    if l_name == 'q':
        break;

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello,"+ formatted_name+"!")

# 4-Transfer list
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, "+name.title()+"!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 首先创建一个列表，其中包含一些要打印的设计
unprited_designs = ['iphone case', 'robot pendent',  'dodecahedron']
complexd_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印的每个设计后，都将其移到列表comleted_models中
while unprited_designs:
    current_design = unprited_designs.pop()
    # 模拟根据设计制作3D打印模型的过程
    print("Print model:"+current_design)
    complexd_models.append(current_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for complexd_model in complexd_models:
    print(complexd_model)

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有 未打印的设计为止
    打印每个设计后，都将其移到 列表completed_models中
    """
    while unprinted_designs:
        current_design = unprited_designs.pop()
        #模拟根据设计制作3D打印模型的过程
        print('Printing model:'+current_design)
        complexd_models.append(current_design)

def show_complexd_models(complexd_models):
    """显示打印好的所有数据"""
    print("\nThe following models have been printed:")
    for complexd_model in complexd_models:
        print(complexd_model)
unprited_designs = ['iphone case', 'robot pendent', 'dodecahedron']
complexd_models = []

print_models(unprited_designs, complexd_models)
show_complexd_models(complexd_models)

# 5_Passing any number of arguments
def make_pizza(*toppings):
    "打印 顾客点的所有配料"
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extar cheese')

def  make_pizza(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following  toppings:")
    for topping in toppings:
        print("-" + topping)
make_pizza('popperoni')
make_pizza('mushrooms','green  peopers','extra chees')