#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Created on: Tues Oct 28 2025
@Author: Saja Noor
@Course: INF 6050
@University: Wayne State University
@Assignment: Group Project: Bookshelf Update Function Test
@Python Version: 3.13.5
@Required Modules: sys, csv
@Description: This code is a test version of a user defined function that will
allow users to add a new book to their bookshelf using csv files.

"""

###########################
# GLOBAL VARIABLES
###########################
#  Import the sys module to allow use of the sys.exit function, allowing the 
#  player to quit at any time.
import sys
#  Import the csv module to allow the program to write player data to a csv
#  file and access said data later
import csv
###########################
# USER-DEFINED FUNCTIONS
###########################
#  With this user-defined function, when a player decides to add a new book or
#  other piece of media the program will run the following lines of code to
#  open their bookshelf csv file and add a new row, filling in each of the
#  prompted fields.
def newBook():
    while True:
        with open("bookshelf.csv", "a", newline="") as csvfile:
            fieldnames = ["Type", "Title", "Author", "Year", "Status"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow(
                {"Type":input("Enter media type(ebook, hardcover, etc.): "),
                 "Title":input("Enter media title: "),
                 "Author":input("Enter media author's name: "),
                 "Year":input("What year was it published in?: "),
                 "Status":input("Enter reading status(TBR, Reading, Finished, "
                                "etc): ")
                })
            enterMedia = input("Would you like to enter another?: ")
            if enterMedia == "Y":
                continue
            elif enterMedia == "Q":
                break
#  With this user-defined function, when a player decides to quit the program 
#  will run the following lines of code to output a goodbye message and end the
#  program.
def quitGame():
    print("\n")
    print("Thanks for playing! See you next time!")
    print("\n")
    sys.exit("Quitting program...")
###########################
# SCRIPT HERE
###########################
#  The following lines prompt the user to answer whether they'd like to enter
#  a new book or if they'd like to quit the program, running each user defined
#  function for each answer respectively.
userEntry = input("Would you like to enter a book?: ")
if userEntry == "Y":
    newBook()
elif userEntry == "Q":
    quitGame()