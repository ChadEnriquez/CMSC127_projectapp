'''
CMSC 127 S3L Group 3 Project
Chad Andrei A. Enriquez
Genevieve D. Penes
Ryan G. Villacorte
'''

import mysql.connector as mariadb

# Connect to MariaDB Platform

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
    print("------------------------------------------------")
    print("   What would you like to do with an expense? ")
    print("------------------------------------------------")
    print("[1] Add an expense")
    print("[2] Delete an expense")
    print("[3] Search an expense")
    print("[4] Update an expense")
    print("[0] Back to main menu")
    print("------------------------------------------------")
    choice = input("Please enter your choice: ")

    if choice == "1":
        print(" In the making ")
    elif choice == "2":
        print(" In the making ")
    elif choice == "3":
        print(" In the making ")
    elif choice == "4":
        print(" In the making ")
    elif choice == "0":
        main_menu()

def adsu_friend():
    print("------------------------------------------------")
    print("   What would you like to do with a friend? ")
    print("------------------------------------------------")
    print("[1] Add a friend")
    print("[2] Delete a friend")
    print("[3] Search a friend")
    print("[4] Update a friend")
    print("[0] Back to main menu")
    print("------------------------------------------------")
    choice = input("Please enter your choice: ")

    if choice == "1":
        print(" In the making ")
    elif choice == "2":
        print(" In the making ")
    elif choice == "3":
        print(" In the making ")
    elif choice == "4":
        print(" In the making ")
    elif choice == "0":
        main_menu()

def adsu_group():
    print("------------------------------------------------")
    print("   What would you like to do with a group? ")
    print("------------------------------------------------")
    print("[1] Add a group")
    print("[2] Delete a group")
    print("[3] Search a group")
    print("[4] Update a group")
    print("[0] Back to main menu")
    print("------------------------------------------------")
    choice = input("Please enter your choice: ")

    if choice == "1":
        print(" In the making ")
    elif choice == "2":
        print(" In the making ")
    elif choice == "3":
        print(" In the making ")
    elif choice == "4":
        print(" In the making ")
    elif choice == "0":
        main_menu()

def payment():
    print("------------------------------------------------")
    print("  Who would you like to accomplish a payment? ")
    print("------------------------------------------------")
    print("[1] A friend")
    print("[2] A group")
    print("[0] Back to main menu")
    print("------------------------------------------------")
    choice = input("Please enter your choice: ")

    if choice == "1":
        print(" In the making ")
    elif choice == "2":
        print(" In the making ")
    elif choice == "0":
        main_menu()

def reports():
    print("------------------------------------------------")
    print("    What report would you like to generate? ")
    print("------------------------------------------------")
    print("[1] View all expenses made within a month")
    print("[2] View all expenses made with a friend")
    print("[3] View all expenses made with a group")
    print("[4] View current balance from all expenses")
    print("[5] View all friends with outstanding balance")
    print("[6] View all groups")
    print("[7] View all groups with an outstanding balance")
    print("[0] Back to main menu")
    print("------------------------------------------------")
    choice = input("Please enter your choice: ")

    if choice == "1":
        print(" In the making ")
    elif choice == "2":
        print(" In the making ")
    elif choice == "3":
        print(" In the making ")
    elif choice == "4":
        print(" In the making ")
    elif choice == "5":
        print(" In the making ")
    elif choice == "6":
        print(" In the making ")
    elif choice == "7":
        print(" In the making ")
    elif choice == "0":
        main_menu()
    
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
        break
    else:
        print("Invalid input. Please try again.")
        continue
    