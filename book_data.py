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

#File Handling with JSON
#Loading the bookshelf or creating a new JSON file 
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

#Saving updated bookshelf to JSON file (rewitten functions have built-in 
#saves after every action)
def save_books(filename):
    try:
        books = load_books(filename)
        
        with open(filename, 'w') as file:
            json.dump(books, file, indent=4)
        print(f"\nBookshelf successfully saved to '{filename}'\n")
    except Exception as e:
        print(f"\nError saving file: '{e}'\n")
    
#Book Management Functions 
#adding a new book to bookshelf
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

#Updating an existing book on bookshelf
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

    #Calling the inputted book 
    book = books[matched_title]

    #New inputs for book 
    print("\nEnter the new values below. Press Enter to keep the "
          "current value.\n")

    for field in ["author", "genre", "year", "form", "status", "rating",
                  "notes"]:
        new_value = input(f"New {field.capitalize()} "
                          "(current: '{book.get(field, '')}'): ").strip()
        if new_value:
            book[field] = new_value
   
    #save changes to JSON
    with open(filename, "w") as f:
        json.dump(books, f, indent=4)

    print(f"Successfully updated '{matched_title}'.")
    return True
    
#Removing a book from bookshelf
def remove_book(filename, title):
    books = load_books(filename) #calling the load_book function 
    
    #Find book by title
    matched_title = None
    for book_title in books:
        if book_title.lower() == title.lower():
            matched_title = book_title
            break 
    
    if matched_title:
        del books[matched_title] #removal of book 
        
        #save changes to JSON 
        with open(filename, "w") as f:
            json.dump(books, f, indent=4)
            
        print(f"Successfully removed '{matched_title}' from your bookshelf.")
        return True 
    
    print(f"Book titled '{title}' not found in your bookshelf.")
    return False

#Finding a book on bookshelf (view-only function)
# finding a book on the bookshelf (an attempt was made -Saja)
def find_books(books, title):
    search_for = input("Which book title would you like to search for?: ")
    for search_for in books:
        print(list(filter(lambda x:x["title"]==search_for, books)))
    if search_for not in books:
        print(search_for, "is not a title present on your bookshelf.")

#Display & Export Functions
#displaying books in table-like format in console (NEEDS REWORKING)
def display_books(filename):
    if not filename:
        print('No books to display.')
        return 
    print('Your Bookshelf')
    print('--'*40)
    print(f"{'Title':30} | {'Author':20} | {'Status':15} | {'Rating':6}")
    print('--'*40)
    for book in filename:
        rating = book['rating'] if book['rating'] is not None else '-'
        print(f"{book['title'][:30]:30} | {book['author'][:20]:20} | "
              f"{book['status'][:15]:15} | {str(rating):6}")
        print('--'*40)
    
#exporting current bookshelf to CSV file for Excel-style viewing
#(creates or replaces 'bookshelf.csv' to this new version) (NEEDS REWORKING)
def export_to_csv(file, filename='bookshelf.csv'):
    if not file:
        print('No books to export.')
        return 
    keys = ['title'][0].keys()
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(['title'])
        print(f"Bookshelf successfully exported to '{filename}.'")
    except Exception as e:
        print(f'Error exporting to CSV: {e}')
