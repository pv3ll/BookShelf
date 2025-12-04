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
 
@Description: [A book shelf for users to add, edit, and delete their books by 
               inputting the metadata for the book. This would be used for 
               eBooks, physical books, audiobooks, and etc.]
"""
import book_data #group-created function module

#section divider
def newline():
    print("-" * 40)
    
#With this user-defined function, the user will be able to view the instructions
#when the choose the option "y" or "yes"
def instructions():
    #How to add a book
    print("\nMain Options:\nAdd a Book: You can add a book by choosing 1 or A.\n")
    print("\tHow to add a book:")
    howto_book_entry = { 
        "Author" : "Enter author name",
        "Genre" : "Enter genre of the book(Fantasy, Fiction, NonFic, etc.)",
        "Year" : "Enter published year", 
        "Form" : "Enter format of the book(Audiobook, Physical, eBook, etc.)", 
        "Status" : "Enter state of completion(Completed, TBR, etc.)", 
        "Rating" : "Rate book on a scale of 1 to 5(1 = Bad, 5 = Awesome)", 
        "Notes" : "Comments or reminders about the book"}   
    for (key,val) in howto_book_entry.items():
       print("\t", key,":", val)
    newline()
    #How to remove a book
    print("To remove a book, choose 2 or R.")
    print("\tTo remove a book, enter the title of the book.\n")
    newline()
    #How to update a book
    print("To Update a Book, choose 3 or U.\n")
    print("To update a book, enter the title of a book. Enter updates in the"
          " needed fields. Example:")
    example_update = {
        "New Author(current: )" : "Enter new author name",
        "New Genre(current: )" : "Enter  new genre of the book(Fantasy, Fiction, NonFic, etc.)",
        "New Year(current: )" : "Enter  new published year", 
        "New Form(current: )" : "Enter  new format of the book(Audiobook, Physical, eBook, etc.)", 
        "New Status(current: )" : "Enter  new state of completion(Completed, TBR, etc.)", 
        "New Rating(current: )" : "New book rating on a scale of 1 to 5(1 = Bad, 5 = Awesome)", 
        "New Notes(current: )" : "New comments or reminders about the book"}
    for (key,val) in example_update.items():
       print("\t", key,":", val)
    newline()
    #Other functions include, saving, finding a book in the collection, and display
    #options.
    print("Some other functions available is finding a book in your collection,"
          " saving your collection to most recent updates and displaying the book"
          " in a CSV or JSON format.\n")
    print("To Find a Book in your collection, choose 4 or F.\n\tTo find the book,"
          " enter the title.\n")
    print("To save your collection to the most recent, choose 5 or S.\n")
    print("To View your collection, choose 6 or X.\n\tThis will export your"
          " collection into a JSON file, with an option to view it as a CSV file.")
    newline()
    print("To quit the program, press Q")
    
#Introduction to the program
print("Welcome to the Book Shelf!\n")
print("You can use this program to add, edit, or delete your books. It can be"
      " used eBooks, physical books, audiobooks, and anything else.")
newline()

#Filename definition 
filename = "books.json"

#This line of code gives users the option to see the instructions or skip it
choice = input("Would you like instructions? Y/N: ").strip().lower()
while choice not in ("y","n"):
    choice = input("Invalid input, please enter Y or N: ").strip().lower()
if choice == "y":
    print(instructions())
elif choice == "n":
    pass
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
    choice = input("\nMake a selection:\n ").strip().lower()

    #Add a book function
    if choice in ("1", "a"):
        print("\nAdd a New Book\n")
        book_data.add_book(filename)
        newline()
        
    #Remove a book function
    elif choice in ("2", "r"):
        print("Remove a Book\n")
        title = input("Enter the title of the book you would like to"
                      " remove: ").strip()
        book_data.remove_book(filename, title)
        newline()
        
    #Update a book function
    elif choice in ("3","u"):
        print("Update a Book\n")
        title = input("Enter the title of the book you want "
                      "to update: ").strip()
        book_data.update_book(filename, title)
        newline()
        
    #Find a book function
    elif choice in ("4", "f"):
        print("Find a Book\n")
        title = input("Enter the title of the book you want "
                      "to find: ").strip()
        book_data.find_book(filename, title)
        newline()
    
    #Save collection function
    elif choice in ("5", "s"):
        print("Saving your Bookshelf...")
        book_data.save_books(filename)
        newline()
    
    #View collection in Python window function
    elif choice in ("6", "v"):
        print("Here is your current Bookshelf:")
        book_data.view_books(filename)
        newline()
    
    #Export collection to CSV file function
    elif choice in ("7", "x"):
        print("Exporting your Bookshelf...")
        book_data.export_to_csv()
        continue
    
    #Quit the shelf (and save option)
    elif choice == "q":
        save_quit = input("Would you like to save your Bookshelf before "
                         "quitting? (Y/N): ").strip().lower()
        if save_quit == "y":
            book_data.save_books(filename)
            print("\nYour BookShelf is safe.\n")
            book_data.quit_shelf()
            break
        elif save_quit == "n":
            book_data.quit_shelf()
            break
        else: 
            print("Invalid input. Please enter Y or N.\n")


