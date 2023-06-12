'''
CMSC 127 S3L Group 3 Project
Chad Andrei A. Enriquez
Genevieve D. Penes
Ryan G. Villacorte
'''

# Connect to MariaDB Platform
import mysql.connector as mariadb

database = mariadb.connect(
    host='localhost', 
    user='user', 
    passwd='pass',
    database='group3' 
    )

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS group3")
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)

cursor.execute("USE group3")

def main_menu():
    
    print("------------------------------------------------")
    print("           Welcome to the main menu! ")
    print("         What do you want to do today? ")    
    print("------------------------------------------------")
    print("[1] Add, Delete, Search, and Update an EXPENSE")
    print("[2] Add, delete, search, and update a FRIEND")
    print("[3] Add, delete, search, and update a GROUP")
    print("[4] Payments and Settlements")
    print("[5] Reports")
    print("[0] Exit")
    print("------------------------------------------------")
    print("\n")

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
    print("\n")
    choice = input("Please enter your choice: ")
    print("\n")

    if choice == "1":
        add_expense()
    elif choice == "2":
        delete_expense()
    elif choice == "3":
        search_expense()
    elif choice == "4":
        update_expense()
    elif choice == "0":
        main_menu()

def add_expense():
    print("------------------------------------------------")
    print("                 Add an expense ")
    print("------------------------------------------------")
    print("[1] Add an expense with friend")
    print("[2] Add an expense with a group")
    print("[0] Back to main menu")
    print("------------------------------------------------")
    print("\n")
    choice = input("Please enter your choice: ")
    print("\n")

    if choice == "1":
        print("------------------------------------------------")
        print("           Add an expense with a friend")
        print("------------------------------------------------")

        # Prompt the user for expense details
        date_incurred = input("Enter the date incurred (YYYY-MM-DD): ")
        expense_payor_first_name = input("Enter the expense payor's first name: ")
        user_id = input("Enter the expense payor's ID: ")
        total_amount = input("Enter the total amount: ")
        is_settled = input("Is the expense settled? (Yes/No): ")
        group_id = input("Enter the group ID: ")

        # Execute the SQL query to insert the expense into the database
        cursor.execute("INSERT INTO expense (date_incurred, expense_payor_first_name, user_id, total_amount, is_settled, group_id) VALUES (%s, %s, %s, %s, %s, %s)", (date_incurred, expense_payor_first_name, user_id, total_amount, is_settled, group_id))
        database.commit()

        print("Expense added successfully!")

    elif choice == "2":
        print("------------------------------------------------")
        print("           Add an expense with a group")
        print("------------------------------------------------")

        # Prompt the user for expense details
        date_incurred = input("Enter the date incurred (YYYY-MM-DD): ")
        expense_payor_first_name = input("Enter the expense payor's first name: ")
        user_id = input("Enter the expense payor's ID: ")
        total_amount = input("Enter the total amount: ")
        is_settled = input("Is the expense settled? (Yes/No): ")
        group_id = input("Enter the group ID: ")

        # Execute the SQL query to insert the expense into the database
        cursor.execute("INSERT INTO expense (date_incurred, expense_payor_first_name, user_id, total_amount, is_settled, group_id) VALUES (%s, %s, %s, %s, %s, %s)", (date_incurred, expense_payor_first_name, user_id, total_amount, is_settled, group_id))
        database.commit()

        print("Expense added successfully!")

    elif choice == "0":
        main_menu()

def delete_expense():
    print("------------------------------------------------")
    print("              Delete an expense ")
    print("------------------------------------------------")
    print("[1] Delete an expense with friend")
    print("[2] Delete an expense with a group")
    print("[0] Back to main menu")
    print("------------------------------------------------")
    print("\n")
    choice = input("Please enter your choice: ")
    print("\n")

    if choice == "1":
        print("------------------------------------------------")
        print("         Delete an expense with friend")
        print("------------------------------------------------")
        expense_id = input("Enter the expense ID: ")
        cursor.execute("DELETE FROM expense WHERE expense_id = %s", (expense_id,))
        database.commit()
        print("Expense deleted successfully!\n")

    elif choice == "2":
        print("------------------------------------------------")
        print("       Delete an expense with a group")
        print("------------------------------------------------")
        expense_id = input("Enter the expense ID: ")
        cursor.execute("DELETE FROM expense WHERE expense_id = %s", (expense_id,))
        database.commit()
        print("Expense deleted successfully!\n")

    elif choice == "0":
        main_menu()

def search_expense():
    print("------------------------------------------------")
    print("            Search an expense ")
    print("------------------------------------------------")
    print("[1] Search an expense with friend")
    print("[2] Search an expense with a group")
    print("[0] Back to main menu")
    print("------------------------------------------------")
    choice = input("Please enter your choice: ")
    print("\n")

    if choice == "1":
        print("------------------------------------------------")
        print("      Search an expense with a friend")
        print("------------------------------------------------")

        # Prompt the user for search criteria
        friend_first_name = input("Enter the friend's first name: ")
        print("\n")

        # Execute the SQL query to search for expenses with the friend
        cursor.execute("SELECT * FROM expense WHERE expense_payor_first_name = %s", (friend_first_name,))
        expenses = cursor.fetchall()

        if len(expenses) > 0:
            print("Expenses found:")
            for expense in expenses:
                print(f"Expense ID: {expense[0]}")
                print(f"Date Incurred: {expense[1]}")
                print(f"Expense Payor's First Name: {expense[2]}")
                print(f"Expense Payor's ID: {expense[3]}")
                print(f"Total Amount: {expense[4]}")
                print(f"Is Settled: {expense[5]}")
                print(f"Group ID: {expense[6]}")
                print("------------------------------------------------")
                print("\n")
        else:
            print("No expenses found.\n")

    elif choice == "2":
        print("------------------------------------------------")
        print("      Search an expense with a group")
        print("------------------------------------------------")

        # Prompt the user for search criteria
        group_id = input("Enter the group ID: ")
        print("\n")

        # Execute the SQL query to search for expenses with the group
        cursor.execute("SELECT * FROM expense WHERE group_id = %s", (group_id,))
        expenses = cursor.fetchall()

        if len(expenses) > 0:
            print("Expenses found:")
            for expense in expenses:
                print(f"Expense ID: {expense[0]}")
                print(f"Date Incurred: {expense[1]}")
                print(f"Expense Payor's First Name: {expense[2]}")
                print(f"Expense Payor's ID: {expense[3]}")
                print(f"Total Amount: {expense[4]}")
                print(f"Is Settled: {expense[5]}")
                print(f"Group ID: {expense[6]}")
                print("------------------------------------------------")
                print("\n")
        else:
            print("No expenses found.\n")
        
    elif choice == "0":

        main_menu()

def update_expense():
    print("------------------------------------------------")
    print("            Update an expense ")
    print("------------------------------------------------")
    print("[1] Update an expense with friend")
    print("[2] Update an expense with a group")
    print("[0] Back to main menu")
    print("------------------------------------------------")
    choice = input("Please enter your choice: ")
    print("\n")

    if choice == "1":
        print("------------------------------------------------")
        print("      Update an expense with a friend")
        print("------------------------------------------------")

        expense_id = input("Enter the expense ID to update: ")
        is_settled = input("Is the expense settled? (Yes/No): ")

        # Execute the SQL query to update the expense in the database
        cursor.execute("UPDATE expense SET is_settled = %s WHERE expense_id = %s", (is_settled, expense_id))
        database.commit()

        print("Expense updated successfully!\n")

    elif choice == "2":
        print("------------------------------------------------")
        print("      Update an expense with a group")
        print("------------------------------------------------")

        expense_id = input("Enter the expense ID to update: ")
        is_settled = input("Is the expense settled? (Yes/No): ")

        # Execute the SQL query to update the expense in the database
        cursor.execute("UPDATE expense SET is_settled = %s WHERE expense_id = %s", (is_settled, expense_id))
        database.commit()

        print("Expense updated successfully!\n")


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
    print("   What would you like to do with a payment? ")
    print("------------------------------------------------")


def reports():
    print("------------------------------------------------")
    print("    What  report would you like to generate? ")
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
    print("\n")

    if choice == "1":
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        print("\n")
        sql_command1 = "SELECT * FROM expense WHERE date_incurred BETWEEN %s AND %s"
        cursor.execute(sql_command1, (start_date, end_date))
        expenses = cursor.fetchall()

        if len(expenses) > 0:
            print("Expenses made within the specified period:")
            print("\n")
            for expense in expenses:
                print(f"Expense ID: {expense[0]}")
                print(f"Group ID: {expense[6]}")
                print(f"Date Incurred: {expense[1]}")
                print(f"Expense Payor's First Name: {expense[2]}")
                print(f"Expense Payor's ID: {expense[3]}")
                print(f"Total Amount: {expense[4]}")
                print(f"Is Settled: {expense[5]}")
                print("------------------------------------------------")
                print("\n")
        else:
            print("No expenses found.\n")

    elif choice == "2":
        sql_command2 = "SELECT * FROM expense WHERE friend_id = %s"
        print(" In the making ")

    elif choice == "3":
        group_id = input("Enter the group ID: ")
        print("\n")
        sql_command2 = "SELECT * FROM expense WHERE group_id = %s"
        cursor.execute(sql_command2, (group_id,))
        expenses = cursor.fetchall()

        if len(expenses) > 0:
            print("Expenses made with the specified group:")
            for expense in expenses:
                print(f"Expense ID: {expense[0]}")
                print(f"Date Incurred: {expense[1]}")
                print(f"Expense Payor's First Name: {expense[2]}")
                print(f"Expense Payor's ID: {expense[3]}")
                print(f"Total Amount: {expense[4]}")
                print(f"Is Settled: {expense[5]}")
                print(f"Group ID: {expense[6]}")
                print("------------------------------------------------")
                print("\n")
        else:
            print("No expenses found.\n")

    elif choice == "4":
        sql_command4 = "SELECT SUM(total_amount) AS 'Current Balance from All Expenses' FROM expense"
        print(" In the making ")
        
    elif choice == "5":
        sql_command5 = "SELECT * FROM groups NATURAL JOIN expense WHERE is_settled='No'"
        cursor.execute(sql_command5)
        result = cursor.fetchall()

        if len(result) > 0: 
            print("Friends with outstanding balance:")
            for row in result:
                print(f"Friend: {row[5]}")
                print(f"Expense ID: {row[3]}")
                print(f"Group ID: {row[0]}")
                print(f"Date Incurred: {row[4]}")
                print(f"Total Amount: {row[7]}")
                print("--------------------")
        else:
            print("No friends with outstanding balance found.")

    elif choice == "6":
        sql_command6 = "SELECT * FROM groups"
        cursor.execute(sql_command6)
        result = cursor.fetchall()

        if len(result) > 0:
            print("All groups:")
            for row in result:
                print(f"Group ID: {row[0]}")
                print(f"Group Name: {row[1]}")
                print(f"No. of Group Members: {row[2]}")
                print("--------------------")
        else:
            print("No groups found.")

    elif choice == "7":
        sql_command7 = "SELECT * FROM groups NATURAL JOIN expense WHERE is_settled='No'"
        cursor.execute(sql_command7)
        result = cursor.fetchall()

        if len(result) > 0:
            print("Groups with outstanding balance:")
            for row in result:
                print(f"Group: {row[1]}")
                print(f"Expense ID: {row[0]}")
                print(f"Date Incurred: {row[4]}")
                print(f"Total Amount: {row[7]}")
                print("--------------------")
        else:
            print("No groups with outstanding balance found.")

    elif choice == "0":
        main_menu()

def main_loop():        
    while True:
        main_menu()
        choice = input("Please enter your choice: ")
        print("\n")

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

main_loop()