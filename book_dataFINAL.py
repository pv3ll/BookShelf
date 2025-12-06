#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
book_data.py 

@Created on: 10/26/2025
@Author: Pearl Vang, Madison Goulet, Saja Noor 
@Course: INF 6050
@University: Wayne State University

@Python Version: 3.9x
@Required Modules: json, os, csv, sys

@Description: Module that handles all data storage, retrieval, and manipulation 
for the BookShelf application.

"""
import json
import os
import csv
import sys

# FILE HANDLING FUNCTIONS WITH JSON
# LOAD bookshelf or create new JSON file 
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
        print("\nBookShelf was empty or invalid. Resetting to an "
              "empty shelf...\n")
        with open(filename, "w") as f:
            json.dump({}, f)
        return {}
# SAVE bookshelf to JSON file - built-in to all book management functions
def save_books(filename):
    try:
        books = load_books(filename)
        with open(filename, "w") as file:
            json.dump(books, file, indent=4)
        print(f"\nBookShelf successfully saved to '{filename}'\n")
    except Exception as e:
        print(f"\nError saving file: '{e}'\n")
    
# BOOK MANAGEMENT FUNCTIONS
# ADD new book
def add_book(filename):
    books = load_books(filename) # Call load_book function 
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
    print(f"\n'{title}' was successfully added to your BookShelf.\n")
# UPDATE existing book
def update_book(filename, title):
    books = load_books(filename) # Call load_book function 
    # Find book by title 
    matched_title = None
    for book_title in books:
        if book_title.lower() == title.lower():
            matched_title = book_title
            break
    if matched_title is None:
        print(f"\nBook titled '{title}' not found.\n")
        return False
    book = books[matched_title] # call inputted book
    # New inputs
    print("\nEnter the new values below. Press Enter to keep the "
          "current value.\n")
    for field in ["author", "genre", "year", "form", "status", "rating",
                  "notes"]:
        new_value = input(
            f"New {field.capitalize()}(current: '{book.get(field, '')}'): "
        ).strip()
        if new_value:
            book[field] = new_value
    # Save changes to JSON
    with open(filename, "w") as f:
        json.dump(books, f, indent=4)
    print(f"\nSuccessfully updated '{matched_title}'.\n")
    return True  
# REMOVE book
def remove_book(filename, title):
    books = load_books(filename) # Call load_book function 
    # Find book by title
    matched_title = None
    for book_title in books:
        if book_title.lower() == title.lower():
            matched_title = book_title
            break 
    if matched_title:
        del books[matched_title] # Removing book 
        # Save changes to JSON 
        with open(filename, "w") as f:
            json.dump(books, f, indent=4)
        print(f"\nSuccessfully removed '{matched_title}' "
              "from your BookShelf.\n")
        return True 
    else:
        print(f"\nBook titled '{title}' not found in your BookShelf.\n")
        return False
# FIND book (view-only function)
def find_book(filename, title):
    books = load_books(filename) # Call load_book function
    # Find book by title
    matched_title = None
    for book_title in books:
        if book_title.lower() == title.lower():
            matched_title = book_title
            break
    if matched_title is None:
        print(f"\nBook titled '{title}' not found.\n")
        return False
    book = books[matched_title] # Retrieving and displaying book dictionary
    print("\nBook Found\n")
    print("-" * 80)
    print("\n")
    print(f"{'Title'} | {'Author'} | {'Genre'} | {'Year'} | "
          f"{'Form'} | {'Status'} | {'Rating'} | {'Notes'} | ")
    print("\n")
    print("-" * 80)
    print("\n")
    print(f"{matched_title} | "
          f"{book.get('author')} | "
          f"{book.get('genre')} | "
          f"{str(book.get('year'))} | "
          f"{book.get('form')} | "
          f"{book.get('status')} | "
          f"{str(book.get('rating'))} | "
          f"{book.get('notes')} | ")
    print("\n")

# DISPLAY & EXPORT FUNCTIONS
# VIEW books directly in Python console 
def view_books(filename):
    books = load_books(filename) # Call load_book function
    if not books:
        print("\nNo books to display.\n")
        return
    print("-" * 80)   
    print("\n")
    print(f"{'Title'} | {'Author'} | {'Genre'} | {'Year'} | "
          f"{'Form'} | {'Status'} | {'Rating'} | {'Notes'} | ")
    print("\n")
    print("-" * 80)
    for title, book in books.items():
        print("\n")
        print(f"{title} | "
              f"{book.get('author')} | "
              f"{book.get('genre')} | "
              f"{str(book.get('year'))} | "
              f"{book.get('form')} | "
              f"{book.get('status')} | "
              f"{str(book.get('rating'))} | "
              f"{book.get('notes')} | ")
        print("\n")
        print("-" * 80)
    print("\nEnd of BookShelf.\n")
# EXPORT bookshelf to CSV for Excel viewing
# Create or replace 'bookshelf.csv'
def export_to_csv(filename="bookshelf.csv"): 
    try:
        # Load JSON file
        with open("books.json") as jf:
            books = json.load(jf)
        if not books:
            print("No books found to export.")
            return
        # Convert dict to list of rows for CSV
        records = []
        for title, info in books.items():
            record = {"title": title}
            record.update(info)
            records.append(record) 
        with open(filename, "w", newline="", encoding="utf-8") as df:
            writer = csv.writer(df)
            # Create headers and rows
            header = [h.capitalize() for h in records[0].keys()]
            writer.writerow(header)
            for record in records:
                writer.writerow(record.values())
            print(f"BookShelf successfully exported to '{filename}'.")
    except Exception as e:
        print(f"Error exporting to CSV: '{e}'")
        
#QUIT program function - quit logic in module
def quit_shelf():
        print("\nSee you next time!\n")
        sys.exit()
