'''for i in range(3):
    print(f"Attempt: {i + 1}")
print("A total of three attempts have been made")

for letter in "Hippopotamus":
    print(letter)


def calculate(a, b):
    print(a + b)

result = calculate(5, 5)
print(result)
'''

try:
    number = int("Hello")
    raise Exception("Simulated crash")
except Exception:
    print("Caught an error")
finally:
    print("This always runs")

def process_customer(customer):
    if "email" not in customer:
        # I am manually triggering an error here
        raise ValueError("Data Error: Customer is missing an email address!")
    
    print(f"Processing email: {customer['email']}")

# This will crash with your custom message
process_customer({"name": "John"}) 

