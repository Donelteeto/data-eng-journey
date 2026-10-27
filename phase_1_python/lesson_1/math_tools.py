def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def find_max(list_of_numbers):
    highest = list_of_numbers[0]
    for i in list_of_numbers:
        if i > highest:
            highest = i
    return highest

# Calling the functions
sub_ops = subtract(12,7)
print(sub_ops)

mul_ops = multiply(4,8)
print(mul_ops)

is_ops = is_even(8)
print(is_ops)

find_ops = find_max([2,5,7,3,0,9,18,78])
print(find_ops)