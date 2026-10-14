first_name = "  john    "
last_name = "SMITH"
full_name = first_name.strip() + " " + last_name
#full_name = full_name.lstrip()

print(f"Formal name: {full_name.title()}")



price = 49.9567
num = 1234567

print(f"The price for the toy is ${price:.2f}")
print(f"The distance of the earth to the moon is about {num:,} miles")