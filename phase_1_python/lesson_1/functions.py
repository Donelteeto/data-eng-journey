# 1. A function with no parameter
def say_hello():
    print("Hello!")


# 2. A function with one parameter
def greet(name):
    print(f"Hello, {name}!")


# 3. A function with two parameters and a print
def add_and_print(a,b):
    print(a+b)

# 4. A function with a return value
def add_and_return(a,b):
    return a+b

# Calling the functions

say_hello()
greet("Julius")
add_and_print(5,9)

result = add_and_return(4,12)
print("The result variable holds:", result)
print("Math with the result:", result * 2)


'''def make_money():
    money = 100

make_money()
print(money)
'''

