person = {
    "name": "Ada Lovelace",
    "age": 36,
    "city": "London",
    "active": True
}

print(person)
print(person["name"])
print(person["active"])

print(person.get("country"))
print(person.get("country", "Unknown"))

person["country"] = "UK"
print(person)

person["age"] = 42
print(person["age"])

del person["active"]
print(person)

print(person.keys())
print(person.values())
print(person.items())
print(len(person))
print("name" in person)