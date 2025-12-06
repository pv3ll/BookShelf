#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created on: [10/23/2025]
@Creators: [Pearl Vang, Madison Goulet, Saja Noor]
@Course: INF 6050
@University: Wayne State University
@Assignment: [Group Project - Book Shelf]
@Python Version: 3.12.5 | packaged by Anaconda, Inc.  
@Required Modules: [book_data]
 
@Description: [A virtual book shelf for users to add, edit, and delete 
               their books by inputting the metadata for the book. This could 
               be used for physical books, eBooks, audiobooks, etc.]
"""
# Group-created module w/ user-defined functions 
import book_data

# Section divider
def newline():
    print("-" * 80)
    
# User-defined function for viewing instructions 
# 'Y' or 'Yes' selection 
def instructions():
    # How to add a book instructions 
    print("\nMain Options")
    print("\nAdd a Book - You can add a book by inputting '1' or 'A'")
    print("\nAdd a book:")
    howto_book_entry = { 
        "Author" : "Enter author name",
        "Genre" : "Enter genre of the book (Fantasy / Fiction / Nonfic, etc.)",
        "Year" : "Enter publication year", 
        "Form" : "Enter format of the book (Physical / eBook / Audiobook)", 
        "Status" : "Enter state of completion (TBR / In Progress / "
                    "Completed)", 
        "Rating" : "Rate book on a scale of 1 to 5 (1 = bad, 5 = awesome)", 
        "Notes" : "Comments or reminders about the book\n"}   
    for (key,val) in howto_book_entry.items():
       print("\t", key,":", val)
    newline()
    # Remove a book instructions
    print("\nRemove a book - You can remove a book by inputting '2' or 'R'")
    print("\nEnter the title of the book you would like to remove.\n")
    newline()
    # Update a book instructions
    print("\nUpdate a book - You can update an existing book by "
          "inputting '3' or 'U'")
    print("\nUpdate a book by entering the title of the book you would "
          "like to update. Enter updates in the desired fields.")
    print ("\nUpdate a book:")
    example_update = {
        "New Author(current: '')" : "New author name",
        "New Genre(current: '')" : "New genre of the book "
                                  "(Fantasy / Fiction / Nonfic, etc.)",
        "New Year(current: '')" : "New publication year", 
        "New Form(current: '')" : "New format of the book "
                                 "(Physical / eBook / Audiobook)", 
        "New Status(current: '')" : "New state of completion "
                                    "(TBR / In Progress / Completed)", 
        "New Rating(current: '')" : "New book rating on a scale of 1 to 5 "
                                    "(1 = bad, 5 = awesome)", 
        "New Notes(current: '')" : "New comments or reminders "
                                    "about the book\n"}
    for (key,val) in example_update.items():
       print("\t", key,":", val)
    newline()
    # Other functions instructions (find, save, display, export)
    print("\nAdditional Functions")
    print("\nAditional functions include finding a book in your BookShelf, "
          "saving the most recent updates, "
          "viewing your BookShelf in the Python console, "
          "and exporting it to view in an Excel format.\n")
    newline()
    print("\nFind a book on your BookShelf by inputting '4' or 'F'")
    print("\nEnter the title of the book you would like to find.\n")
    newline()
    print("\nSave your BookShelf to the most recent version by "
          "inputting '5' or 'S'\n")
    newline()
    print("\nView your BookShelf in the Python console by "
          "inputting '6' or 'V'\n")
    newline()
    print("\nExport your BookShelf into a CSV file and view in Excel by "
          "inputting '7' or 'X'\n")
    newline()
    print("\nTo quit the program, press 'Q'\n")
    newline()
    
# Introduction to the program
print("\nWelcome to the BookShelf!")
print("\nYou can use this program to add, edit, or delete your books. It can "
      "be used eBooks, physical books, audiobooks, or anything else "
      "you would like to track!\n")
newline()

# Filename definition 
filename = "books.json"

# Option to view instructions or skip to main menu
choice = input("\nWould you like instructions? Y/N: ").strip().lower()
while choice not in ("y","n"):
    choice = input("\nInvalid input, please enter Y or N: ").strip().lower()
if choice == "y":
    (instructions())
elif choice == "n":
    pass

# Main menu loop
while True: 
    print("\nMain Menu:")
    print("1. (A)dd a Book")
    print("2. (R)emove a Book")
    print("3. (U)pdate a Book")
    print("4. (F)ind a Book")
    print("5. (S)ave your BookShelf")
    print("6. (V)iew your BookShelf")
    print("7. E(X)port to CSV and Excel")
    print("(Q)uit")
    choice = input("\nMake a selection: ").strip().lower()
    #Add a book function
    if choice in ("1", "a"):
        print("\nAdd a New Book\n")
        book_data.add_book(filename)
        newline()
    #Remove a book function
    elif choice in ("2", "r"):
        print("\nRemove a Book\n")
        title = input("\nEnter the title of the book you would like to "
                      "remove: ").strip()
        book_data.remove_book(filename, title)
        newline()
    #Update a book function
    elif choice in ("3","u"):
        print("\nUpdate a Book\n")
        title = input("\nEnter the title of the book you would like to "
                      "update: ").strip()
        book_data.update_book(filename, title)
        newline()   
    #Find a book function
    elif choice in ("4", "f"):
        print("\nFind a Book\n")
        title = input("\nEnter the title of the book you would like to "
                      "find: ").strip()
        book_data.find_book(filename, title)
        newline()
    #Save collection function
    elif choice in ("5", "s"):
        print("\nSaving your BookShelf...\n")
        book_data.save_books(filename)
        newline()
    #View collection in Python window function
    elif choice in ("6", "v"):
        print("\nHere is your current BookShelf\n")
        book_data.view_books(filename)
        newline()
    #Export collection to CSV file function
    elif choice in ("7", "x"):
        print("\nExporting your BookShelf...\n")
        book_data.export_to_csv()
        newline()
    #Quit the shelf (and save option)
    elif choice == "q":
        save_quit = input("\nWould you like to save your BookShelf before "
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
            print("\nInvalid input. Please enter Y or N.")
