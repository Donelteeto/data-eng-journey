def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    #print("Operation successfully completed")
div_ops = divide(10, 0)
print(div_ops)