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

#print(customers)
#print(customers[1]["name"])
#print(customers[0]["email"])

#for key in customers:
    #print(key["name"])

# Testing inner loop
for customer in customers:
    for keys, value in customer.items():
        print(keys, value)


