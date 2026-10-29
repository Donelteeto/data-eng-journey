with open("employee.csv", "w") as file:
    file.write("id,name,department,salary\n")
    file.write("1,John Doe,Engineering,75000\n")
    file.write("2,Jane Smith,Marketing,65000\n")
    file.write("3,Michael Johnson,Engineering,80000\n")
    file.write("4,Emily Davis,HR,60000\n")
    file.write("5,Michael Brown,Marketing,68000\n")

print("CSV file created!")