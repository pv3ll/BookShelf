#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
book_data.py 

@Created on: 10/26/2025
@Author: Pearl Vang, Madison Goulet, Saja Noor 
@Course: INF 6050
@University: Wayne State University

@Python Version: 3.9x
@Required Modules: json, os, csv

@Description: Module that handles all data storage, retrieval, and manipulation 
for the BookShelf application.

"""
import json
import os
import csv
import sys

#FILE HANDLING WITH JSON
#LOADING the bookshelf or CREATING a new JSON file 
def load_books(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
                json.dump({}, f)
        return {}
    try:
        with open(filename, "r") as f:
            data = json.load(f)
           
            if isinstance(data, dict):
                return data
            else:
                print("\nAn error occured when pulling the file. The data in "
                      "the file was not deleted. Please inspect the file "
                      "manually.\n")
                return {}
    except json.JSONDecodeError:
        print("\nBookshelf was empty of invalid. Resetting to an "
              "empty shelf...\n")
        with open(filename, "w") as f:
            json.dump({}, f)
        return {}

#SAVING updated bookshelf to JSON file (rewitten functions have built-in 
#saves after every action)
def save_books(filename):
    try:
        books = load_books(filename)
        with open(filename, 'w') as file:
            json.dump(books, file, indent=4)
        print(f"\nBookshelf successfully saved to '{filename}'\n")
    except Exception as e:
        print(f"\nError saving file: '{e}'\n")
    
#BOOK MANAGEMENT FUNCTIONS
#ADDING a new book to bookshelf
def add_book(filename):
    books = load_books(filename) #calling the load_book function 
    title = input("Title: ").strip()
    new_book = {
        "author" : input("Author: ").strip(),
        "genre" : input("Genre: ").strip(),
        "year" : input("Publication Year: ").strip(),
        "form" : input("Form (Physical / eBook / Audiobook): ").strip(),
        "status" : input("Status (Completed / In Progress / TBR): ").strip(),
        "rating" : input("Rating (1-5, optional): ").strip(),
        "notes" : input("Notes (optional): ").strip(),
        }
    books[title] = new_book
    with open(filename, "w") as f:
        json.dump(books, f, indent=4)
    print(f"\n'{title}' was successfully added to your bookshelf.\n")

#UPDATING an existing book on bookshelf
def update_book(filename, title):
    books = load_books(filename) #calling the load_book function 
    #Find the book by title 
    matched_title = None
    for book_title in books:
        if book_title.lower() == title.lower():
            matched_title = book_title
            break
    if matched_title is None:
        print(f"Book titled '{title}' not found.\n")
        return False
    book = books[matched_title] #calling the inputted book
    #New inputs for book 
    print("\nEnter the new values below. Press Enter to keep the "
          "current value.\n")
    for field in ["author", "genre", "year", "form", "status", "rating",
                  "notes"]:
        new_value = input(
            f"New {field.capitalize()}(current: '{book.get(field, '')}'): "
        ).strip()
        if new_value:
            book[field] = new_value
    #save changes to JSON
    with open(filename, "w") as f:
        json.dump(books, f, indent=4)
    print(f"Successfully updated '{matched_title}'.")
    return True
    
#REMOVING a book from bookshelf
def remove_book(filename, title):
    books = load_books(filename) #calling the load_book function 
    #Find book by title
    matched_title = None
    for book_title in books:
        if book_title.lower() == title.lower():
            matched_title = book_title
            break 
    if matched_title:
        del books[matched_title] #removing the book 
        #save changes to JSON 
        with open(filename, "w") as f:
            json.dump(books, f, indent=4)
        print(f"Successfully removed '{matched_title}' from your bookshelf.")
        return True 
    else:
        print(f"Book titled '{title}' not found in your bookshelf.")
        return False

#FINDING a book on bookshelf (view-only function)
def find_book(filename, title):
    books = load_books(filename) #callling the load_book function
    #Find book by title
    matched_title = None
    for book_title in books:
        if book_title.lower() == title.lower():
            matched_title = book_title
            break
    if matched_title is None:
        print(f"Book titled '{title}' not found.\n")
        return False
    book = books[matched_title] #Retrieving and displaying book dictionary
    print(f"\n Book Found: {matched_title}\n")
    for field, value in book.items():
        print(f"{field.capitalize()}: {value}")
        print("-" * 40)

#DISPLAY & EXPORT FUNCTIONS
#VIEWING books directly in Python console 
def view_books(filename):
    books = load_books(filename) #calling the load_book function
    if not books:
        print("No books to display.\n")
        return
    print("-" * 40)    
    print(f"{'Title'} | {'Author'} | {'Genre'} | {'Year'} | "
          f"{'Form'} | {'Status'} | {'Rating'} | {'Notes'} | ")
    print("-" * 40)
    for title, book in books.items():
        print(f"{title} | "
              f"{book.get('author')} | "
              f"{book.get('genre')} | "
              f"{str(book.get('year'))} | "
              f"{book.get('form')} | "
              f"{book.get('status')} | "
              f"{str(book.get('rating'))} | "
              f"{book.get('notes')} | ")
        print("-" * 40)
    print("End of bookshelf.\n")
    
#exporting current bookshelf to CSV file for Excel-style viewing
#(creates or replaces 'bookshelf.csv' to this new version) (NEEDS REWORKING)
def export_to_csv(file, filename='bookshelf.csv'):
    if not file:
        print('No books to export.')
        return 
    try:
        with open("books.json") as jf:
            jsonDump = json.load(jf)
        df = open("books.csv", 'w', newline='')
        cw = csv.writer(df)
        c = 0
        for data in jsonDump:
            if c == 0:
                header = data.keys()
                cw.writerow(header)
                c += 1
            cw.writerow(data.values())
        df.close()
        print(f"Bookshelf successfully exported to '{filename}.'")
    except Exception as e:
        print(f'Error exporting to CSV: {e}')
        
#QUIT program function (quit logic in module)
def quit_shelf():
        print("\nSee you next time!\n")
        sys.exit()
