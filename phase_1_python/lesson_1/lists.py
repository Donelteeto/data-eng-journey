fruits = ["apple", "banana", "cherry", "guava"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])
print(fruits[:3])
print(fruits[0:3])
print(len(fruits))
print("banana" in fruits)

fruits.append("mango")
print(fruits)

fruits.insert(2, "grapes")
print(fruits)

fruits.remove("banana")
print(fruits)

popped = fruits.pop()
print(f"Removed: {popped}")
print(fruits)

print(fruits[100])