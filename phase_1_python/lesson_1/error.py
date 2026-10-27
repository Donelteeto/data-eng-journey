# 1. Catching a ValueError
try:
    age = int("twenty")
    print(f"Age is {age}")
except ValueError:
    print("Error: You must type a number, not a word!")


# 2. Catching a FileNotFoundError
try:
    with open("customs.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File cannot be found!")

print("The program continues running!")