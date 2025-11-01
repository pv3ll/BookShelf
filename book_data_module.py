#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
book_data.py 

@Created on: 10/26/2025
@Author: Madison Goulet
@Course: INF 6050
@University: Wayne State University

@Python Version: 3.9x
@Required Modules: json, os, csv

@Description: Module that handles all data storage, retrieval, and manipulation for the BookShelf application.

"""
import json
import os
import csv

#File Handling with JSON
#loading the re-existing bookshelf json file 
#(opens json file already created by application or starts the user with an empty bookshelf)
#(Returns a list of book dictionaries)
def load_books(filename='books.json'):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. You are starting with an empty bookshelf.")
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            books = json.load(file)
            print(f"Successfully loaded {len(books)} books from '{filename}.'")
            return books
    except Exception as e:
        print(F'Unexpected error loading file: {e}')
  
#saving updated bookshelf json file
#(adds new entries or updated existings one and saves to json file)
#(to be called at the end of the main script to save user data for next session)
def save_books(books, filename='books.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(books, file)
        print(f"Bookshelf successfully saved to '{filename}.'")
    except Exception as e:
        print(f'Error saving file: {e}')
    
#Book Management Functions 
#adding a new book to bookshelf
#(only updates the in-memory list, must use save_books() after to make changes permanent)
#(user input and prompts for book details will go in main script)
def add_book(books, title, author, year, form, status='Not Started', rating=None, notes=None): 
    new_book = {
       'title': title, 
       'author': author,
       'year': year, 
       'form': form, 
       'status': status, 
       'rating': rating, 
       'notes': notes
        }
    books.append(new_book)
    print(F"Successfully added '{title} by {author}.")
    return books 
    
#updating an existing book on bookshelf
#(only updates the in-memory list, must use save_books() after to make changes permanent)
#(user input and prompts for book details will go in main script)
def update_book(books, title, updated_info):
    for book in books:
        if book['title'].lower() == title.lower():
            book.update(updated_info)
            print(f"Successfully updated '{title}.'")
            return True 
    print(f"Book titled '{title}' not found.")
    return False 
    
    
#removing a book from bookshelf
#(only updates the in-memory list, must use save_books() after to make changes permanent)
#(user input and prompts for book details will go in main script)
def remove_book(books, title):
    for book in books:
        if book['title'].lower() == title.lower():
            books.remove(book)
            print(f"Removed '{title}' from bookshelf.")
            return True
    print(f"Book titled '{title}' not found.")
    return False 

#Display & Export Functions
#displaying books in table-like format in console
#(shows in Python all current books on bookshelf, quick and easy way to see bookshelf)
#(':number' is the spacing of the table)
def display_books(books):
    if not books:
        print('No books to display.')
        return 
    print('Your Bookshelf')
    print('--'*40)
    print(f"{'Title':30} | {'Author':20} | {'Status':15} | {'Rating':6}")
    print('--'*40)
    for book in books:
        rating = book['rating'] if book['rating'] is not None else '-'
        print(f"{book['title'][:30]:30} | {book['author'][:20]:20} | "
              f"{book['status'][:15]:15} | {str(rating):6}")
        print('--'*40)
    
#exporting current bookshelf to CSV file for Excel-style viewing
#(creates or replaces 'bookshelf.csv' to this new version)
def export_to_csv(books, filename='bookshelf.csv'):
    if not books:
        print('No books to export.')
        return 
    keys = books[0].keys()
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(books)
        print(f"Bookshelf successfully exported to '{filename}.'")
    except Exception as e:
        print(f'Error exporting to CSV: {e}')
