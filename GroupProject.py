#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created on: [10/23/2025]
@Creators: [Pearl Vang, Madison Goulet, Saja Noor]
@Course: INF 6050
@University: Wayne State University
@Assignment: [Group Project - Book Shelf]
@Python Version: 3.12.5 | packaged by Anaconda, Inc.  
@Required Modules: [os, csv, json, sys]
 
@Description: [A book shelf for users to add, edit, and delete their books by inputting the metadata for the book. This would be used for eBooks, physical books, audiobooks, and etc.]
"""
#section divider
def newline():
    print("-" * 25)

#Introduction to the program

print("Welcome to the Book Shelf!\n")
print("You can use this program to add, edit, or delete your books. It can be used eBooks, physical books, audiobooks, and anything else.")
newline()

#This line of code gives users the option to see the instructions or skip it
choice = input("Would you like instructions? Y/N: ").strip().lower()
while choice not in ("y","n"):
    choice = input("Invalid input, please enter Y or N: ").strip().lower()
if choice == "Y":
    print("Showing instructions...")
elif choice == "N":
    print("Please choose 1(A), 2(D), 3(U), 4(F), 5(S), 6(X), or Q for Quit.")

#How to add a book
print("\nMain Options:\nAdd a Book: You can add a book by choosing 1 or A.\n")
print("\tHow to add a book:")

howto_book_entry = {
   "Title" : "Enter title of the book", 
    "Author" : "Enter author name",
    "Genre" : "Enter genre of the book(Fantasy, Fiction, NonFic, etc.)",
    "Year" : "Enter published year", 
    "Form" : "Enter format of the book(Audiobook, Physical, eBook, etc.)", 
    "Status" : "Enter state of completion(Completed, TBR, etc.)", 
    "Rating" : "Rate the book on a scale of 1 to 5(1 = bad, 5 = Awesome)", 
    "Notes" : "Enter any comments or reminders about the book"}
    
for (key,val) in howto_book_entry.items():
   print("\t", key,":", val)

newline()

#How to remove a book
print("To remove a book, choose 2 or R.")
print("\tTo remove a book, enter the title of the book.\n")
newline()
#How to update a book
print("To Update a Book, choose 3 or U.\n")
print("To update a book, enter the title of a book. Enter updates in the needed fields. Example:")

example_update = {
    "Title" : "", 
    "Author" : "",
    "Genre" : "",
    "Year" :"", 
    "Form" : "", 
    "Status" : "Completed", 
    "Rating" : "4", 
    "Notes" : "This book was okay."}

for (key,val) in example_update.items():
   print("\t", key,":", val)
newline()

#Other functions include, saving, finding a book in the collection, and display options.
print("Some other functions available is finding a book in your collection, saving your collection to most recent updates and displaying the book in a CSV or JSON format.\n")
print("To Find a Book in your collection, choose 4 or F.\n\tTo find the book, enter the title.\n")
print("To save your collection to the most recent, choose 5 or S.\n")
print("To View your collection, choose 6 or X.\n\tThis will export your collection into a JSON file, with an option to view it as a CSV file.")

newline()
print("To quit the program, press Q")

#Menu Loop
while True: 
    print("Main Menu:")
    print("1. (A)dd a Book")
    print("2. (R)emove a Book")
    print("3. (U)pdate a Book")
    print("4. (F)ind a Book")
    print("5. (S)ave your Collection")
    print("6. (V)iew your Collection")
    print("7. E(X)port to CSV")
    print("(Q)uit")

    choice = input("\nMake a selection: ").strip().lower()
    newline()

#Add a book function
    if choice in ("1", "a"):
        print("Add a New Book:\n")
        
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        genre = input("Genre: ").strip()
        year = input("Publication Year: ").strip()
        form = input("Form (Physical / eBook / Audiobook): ").strip()
        status = input("Status (Completed / In Progress / TBR): ").strip()
        
        rating_input = input("Rating (1-5, optional)").strip()
        rating = rating_input if rating_input else None
        
        notes_input = input("Notes (optional): ").strip()
        notes = notes_input if notes_input else None
    
        book_data.add_book(books, title, author, genre, year, form, status, rating, notes)
    
        newline()

    #Remove a book function
    elif choice in ("2", "r"):
        print("Remove a Book:\n")
        title = input("Enter the title of the book you would like to remove: ").strip()
        
        book_data.remove_book(books, title)
        
        newline()
    
    #Update a book function
    elif choice in ("3","u"):
        print("Update a Book:\n")
        title = input("Enter the title of the book you would like to update: ").strip()
        
        print("\nEnter the new values below. Press Enter to keep the current value.\n")
        
        updated_info = {}
        for field in ["author", "genre", "year", "form", "status", "rating", "notes"]:
            new_value = input(f"New {field.capitalize()}: ").strip()
            if new_value:
                updated_info[field] = new_value
        
        book_data.update_book(books, title, updated_info)
        
        newline()
        
    #Find a book function (this function is not in the module -- add it? )
    elif choice in ("4", "f"):
 
               
    #Save collection function (needs function added)
    elif choice in ("5", "s"):
        
    #View collection in Python window function (needs function added)
    elif choice in ("6", "v"):
    
    #Export collection to CSV file function (needs function added)
    elif choice in ("7", "x"):
    
    #Quit function
    elif choice == "q":
        print ("Saving your BookShelf before exit...")
        book_data.save_books(books)
        print("\nYour BookShelf is safe. Goodbye!\n")
        break

