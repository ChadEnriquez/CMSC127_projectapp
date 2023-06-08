'''
CMSC 127 S3L Group 3 Project
Chad Andrei A. Enriquez
Genevieve D. Penes
Ryan G. Villacorte
'''

import mysql.connector as mariadb

# Connect to MariaDB Platform
database = mariadb.connect(
    user="user",
    password="useruser",
    host="localhost",
    port="3306",
    )

cursor = database.cursor()
cursor

def main_menu():
    
    print("------------------------------------------------")
    print("           Welcome to the main menu! ")
    print("         What do you want to do today? ")    
    print("------------------------------------------------")
    print("[1] Add, Delete, Search, and Update an EXPENSE")
    print("[2] Add, delete, search, and update a FRIEND")
    print("[3] Add, delete, search, and update a GROUP")
    print("[4] Accomplish payment")
    print("[5] Reports")
    print("[0] Exit")
    print("------------------------------------------------")

def adsu_expense():
    print(" In the making ")

def adsu_friend():
    print(" In the making ")

def adsu_group():
    print(" In the making ")

def payment():
    print(" In the making ")

def reports():
    print(" In the making ")

while True:
    main_menu()
    choice = input("Please enter your choice: ")
    if choice == "1":
        adsu_expense()
    elif choice == "2":
        adsu_friend()
    elif choice == "3":
        adsu_group()
    elif choice == "4":
        payment()
    elif choice == "5":
        reports()
    elif choice == "0":
        print("------------------------------------------------")
        print("       Have a wonderful day! Goodbye! ")
        print("------------------------------------------------")
        break