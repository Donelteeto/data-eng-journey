books = [
    {
        "title": "The Spy Who Loved Me",
        "author": "Roger Moore",
        "year": 1996,
        "available": False
    },
    {
        "title": "Gold Finger",
        "author": "Pierce Brosnan",
        "year": 1990,
        "available": False
    },
    {
        "title": "48 Laws of Power",
        "author": "Robert Greene",
        "year": 2000,
        "available": True
    },
    {
        "title": "The Blood of Jesus",
        "author": "Rev Tunde Bolanta",
        "year": 2024,
        "available": True
    },
    {
        "title": "The Covenant Marriage",
        "author": "Pst Femi Ogunbanwo",
        "year": 2023,
        "available": True
    }
]

#Section prints the full catalog of books
print("-" * 3 + " " + "Library Catalog" + " " + "-" * 3)
for number, book in enumerate(books, start=1):
    line = f"{number}. {book['title']} by {book['author']} {(book['year'])} -"
    if book['available'] == True:
        print(line + " Available")
    else:
        print(line + " Checked Out")


#Section searches books published since 2000
print("-" * 65)
print("-" * 3 +" "+ "Books Published Since 2000" + " " + "-" * 3)
counter = 1
for book in books:
    if book["year"] >= 2000:
        print(f"{counter}. {book['title']} {book['author']} {book['year']}")
        counter += 1

#Section searches book by title
print("-" * 65)
print("-"*3 +" "+"Book Search By Title"+" "+"-"*3)
search_title = "49 Laws of Power"
found = False
for book in books:
    if book["title"] == search_title:
        print(f"Found: {book['title']} by {book['author']}")
        found = True
        break
    #if search_title == "48 Laws of Power":
        #print(f"Found: {book['title']} by {book['author']} ")
        #print(book)
if not found:
    print("No book found with that title")

#Section calculates total number of books, available books, checked out books and the oldest book by year
print("-" * 65)
print("-"*3+" "+"Statistics"+" "+"-"*3)
print(f"Total number of books is: {len(books)}")
available_book = 0
for book in books:
    if book["available"] == True:
        available_book += 1
print(f"The number of available books are: {available_book}")

checked_out_book = 0
for book in books:
    if book["available"] == False:
        checked_out_book += 1
print(f"The number of checked-out books are: {checked_out_book}")

oldest_book = books[0]
for book in books:
    if book["year"] < oldest_book["year"]:
        oldest_book = book
print(f"The oldest book by year is: {oldest_book['title']} by {oldest_book['author']} in {oldest_book['year']}")

#Section validates the availability check
print("-" * 65)
print("-"*3+" "+"Availability check"+" "+"-"*3)
for book in books:
    if book["available"] == True:
        print(f"The book {book['title']} is available")
    else:
        print(f"The book {book['title']} is checked out")

print(f"You have {checked_out_book} books checked out")

#Section calculates the average publication year
print("-" * 65)
print("-"*3+" "+"Average Publication year"+" "+"-"*3)
total_publication_year = 0

for book in books:
    total_publication_year += book["year"]
average_year = total_publication_year / len(books)
print(round(average_year))

