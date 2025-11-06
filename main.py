"""
@Created on: [10/23/2025]
@Creators: [Pearl Vang, Madison Goulet, Saja Noor]
@Course: INF 6050
@University: Wayne State University
@Assignment: [Group Project - Book Shelf]
    
@Python Version: 3.12.5 | packaged by Anaconda, Inc.  
@Required Modules: []

@Description: [A book shelf for users to add, edit, and delete their books by inputting the metadata for the book. This would be used for eBooks, physical books, audiobooks, and etc.]
"""
#Introduction to the program and what it does

print("Welcome to the Book Shelf!\n")
print("You can use this program to add, edit, or delete your books. It can be used eBooks, physical books, audiobooks, and anything else.\n")
print("Please input the information about your book!")
print("----"*5)

#Show total number of books
def totalBooks(): 
    for entry in totalBooks:
        if new_book in totalBooks: 
            totalBooks + 1
        elif book_delete in totalBooks: 
            totalBooks - 1
        else:
            print("You have", totalBooks, "in your collection")

#book questions formatted in a dictionary
new_book = {
    "Title" : " ",
    "Author" : " ",
    "Year Published" : " ",
    "Genre" : " ",
    "Completion": " "
}

for key in new_book:
    new_book[key] = input(f"{key}:")
for key, val in new_book.items():
    print(f"{key} {val}")

#Ending of program prompt

print("See You Next Time!")
