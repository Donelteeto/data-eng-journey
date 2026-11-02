# 1. Normal function vs Lambda function
def multiply(a, b):
    return a * b

test_1 = multiply(5,4)
print(f"Normal function: {test_1}")

multiply_lambdas = lambda a, b: a * b
print(f"Lambda function: {multiply_lambdas(5,4)}")

# 2. Sortiing with Lambda
products = [
    {
        "name": "Laptop",
        "price": 450000
    },
    {
        "name": "Mouse",
        "price": 2000
    },
    {
        "name": "Keyboard",
        "price": 4000
    }
]

# sort by price
sorted_price = sorted(products, key=lambda x: x["price"])
print(sorted_price)

# 3. Using map() 
words = ["hello", "world", "python"]
new_word_upper = list(map(lambda word: word.upper(), words))
print(new_word_upper)