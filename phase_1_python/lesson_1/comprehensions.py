numbers = [1, 2, 3, 4, 5, 6, 7, 8]
multiples_num = [num * 10 for num in numbers]
print(multiples_num)

words = ["hello", "world", "python"]
upper_case_words = [i.upper() for i in words]
print(upper_case_words)

words = ["hell", "world", "python", "is", "great"]
new_words = [i for i in words if len(i) > 4]
print(new_words)

names = ["john", "jane", "mike"]
new_names = {name : name.title() for name in names}
print(new_names)

name_length = {name: len(name) for name in names}
print(name_length)