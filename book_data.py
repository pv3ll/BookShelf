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
#loading the pre-existing bookshelf json file 
def load_books(filename):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. You are starting with an empty "
              f"bookshelf.")
        try:
            with open(filename, 'w') as file:
                pass
        except Exception as e:
            print(F'Unexpected error loading {file}: {e}')
        return []
  
#saving updated bookshelf json file
#(adds new entries or updated existings one and saves to json file)
#(to be called at the end of the main script to save user data for next
#session)
def save_books(filename):
    try:
        with open(filename, 'w') as file:
            json.dump(filename)
        print(f"Bookshelf successfully saved to '{filename}.'")
    except Exception as e:
        print(f'Error saving file: {e}')
    
#Book Management Functions 
#adding a new book to bookshelf
def add_book(filename):
    new_book = {
        input("Title: ").strip():[
        {"author" : input("Author: ").strip(),
        "genre" : input("Genre: ").strip(),
        "year" : input("Publication Year: ").strip(),
        "form" : input("Form (Physical / eBook / Audiobook): ").strip(),
        "status" : input("Status (Completed / In Progress / TBR): ").strip(),
        "rating" : input("Rating (1-5, optional): ").strip(),
        "notes" : input("Notes (optional): ").strip(),
        }]}
    try:
        with open(filename, "r") as file:
            print(file)
            bookshelf = json.load(file)
        bookshelf.append(new_book)
        with open(filename, "w") as file:
            json.dump(bookshelf, file)
    except:
        with open(filename, "w") as file:
            json.dump(new_book, file)
    
#updating an existing book on bookshelf
#With add-book changes, title acts as key for each book. This likely impacts this function ****
def update_book(filename, title, updated_info):
    for book in filename:
        if book['title'].lower() == title.lower():
            book.update(updated_info)
            print(f"Successfully updated '{title}.'")
            return True 
    print(f"Book titled '{title}' not found.")
    return False 
    
#removing a book from bookshelf
def remove_book(filename, title):
    for book in filename:
        if ['title'].lower() == title.lower():
            filename.remove("tile")
            print(f"Removed '{title}' from bookshelf.")
            return True
    print(f"Book titled '{title}' not found.")
    return False 

#Display & Export Functions
#displaying books in table-like format in console
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
#(creates or replaces 'bookshelf.csv' to this new version)
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
        
# finding a book on the bookshelf (an attempt was made -Saja)
def find_books(books, title):
    search_for = input("Which book title would you like to search for?: ")
    for search_for in books:
        print(list(filter(lambda x:x["title"]==search_for, books)))
    if search_for not in books:
        print(search_for, "is not a title present on your bookshelf.")
