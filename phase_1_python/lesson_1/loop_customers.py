customers = [
    {
        "name": "John Doe",
        "email": "johndoe@gmail.com",
        "age": 37
    },
    {
        "name": "Jane Doe",
        "email": "janedoe@yahoo.com",
        "age": 36
    },
    {
        "name": "Stephanie Cochton",
        "email": "stephcoch@gmail.com",
        "age": 45
    }
]

for customer in customers:
    line = f"Name: {customer['name']}, Age: {customer['age']}, Email: {customer['email']}"
    
    if customer["age"] >= 40:
        line += " (senior citizen)"
    print(line)