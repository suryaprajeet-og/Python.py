# #####################################################################
# PROJECT 6: LIBRARY MANAGEMENT SYSTEM (FUNCTION-BASED)
# #####################################################################

name = input(" Enter Customer name: ")
print(" Welcome to The Great Library, ", name)

library = [
    {"title": "Mother", "author": "Lakshmi", "availability": "yes"},
    {"title": "Sports", "author": "Phani", "availability": "yes"},
    {"title": "Coding", "author": "ChatGPT", "availability": "yes"},
    {"title": "Harry Potter", "author": "J.K. Rowling", "availability": "yes"}
]

def add_book():
    while True:
        title = input(" Enter Book Title: ")
        author = input(" Enter author name: ")
        availability = "yes"
        new_book = {"title": title, "author": author, "availability": availability}
        library.append(new_book)
        print(library)
        return

def view_library():
    print(library)

def search_book():
    title = input(" Enter Title of Book: ")
    for book in library:
        if book["title"] == title:
            print(book)
            break
    else:
        print(f" No Book with, {title}, Title found ")
    return

def borrow_book():
    title = input(" Enter Title of The Book: ")
    for book in library:
        if book["title"] == title:
            if book["availability"] == "yes":
                print(" Book found! ")
                print(" Book borrowed Successfully! ")
                book["availability"] = "no"
                break
            else:
                print(" Book Unavailable! ")
                break
    else:
        print(" Book not found! ")

def return_book():
    title = input(" Enter Book Title: ")
    for book in library:
        if book["title"] == title:
            if book["availability"] == "no":
                print(" Book Returned Successfully! ")
                book["availability"] = "yes"
            else:
                print(" Book not Borrowed by anyone for return! ")
            break
    else:
        print(" Book Not Found! ")
    return

def delete_book():
    title = input(" Enter book Title: ")
    for book in library:
        if book["title"] == title:
            print(" Book Found")
            print(" Book Deleted successfully")
            library.remove(book)
            break
    else:
        print(" Book not found")
    return

def total_books():
    print(len(library))

def save_data():
    with open("library.txt", "w") as file:
        for book in library:
            file.write(book["title"] + "," + book["author"] + "," + book["availability"] + "\n")
    print(" Data Saved Successfully! ")

def load_data():
    library.clear()
    with open("library.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            new_books = {"title": data[0], "author": data[1], "availability": data[2]}
            library.append(new_books)
        print(" data loaded successfully! ")
        print(library)

def available_books():
    for book in library:
        if book["availability"] == "yes":
            print(book)
            break
    else:
        print(" No book available")
    return

while True:
    choice = input(" Enter 1. Add Book or 2. View Library or 3. Search Book or 4. Borrow Book or 5. Return Book or 6. Delete Book or 7. Total Books or 8. Save Data or 9. Load Data or 10. Available Books or 11. Exit: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_library()

    elif choice == "3":
        search_book()

    elif choice == "4":
        borrow_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        total_books()

    elif choice == "8":
        save_data()

    elif choice == "9":
        load_data()

    elif choice == "10":
        available_books()

    elif choice == "11":
        print(" Exit Successful! ")
        break

    else:
        print(" Invalid Option! ")


