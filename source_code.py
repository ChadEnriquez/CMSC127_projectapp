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
    else:
        print("Invalid choice. Please try again.\n")

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
    else:
        print("Invalid choice. Please try again.\n")

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
    else:
        print("Invalid choice. Please try again.\n")

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
    else:
        print("Invalid choice. Please try again.\n")
        
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
    else:
        print("Invalid choice. Please try again.\n")

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
        AddFriend()
    elif choice == "2":
        DeleteFriend()
    elif choice == "3":
        SearchFriend()
    elif choice == "4":
        UpdateFriend()
    elif choice == "0":
        main_menu()


def Enterfirst_name(): #Function that adds first name
    firstname = input("\nEnter first name (Maximum of 25 characters): ") #Input from the user
    if (len(firstname)>25): #length of the first name
        print("\n First name exceeds the amount of character needed. Try again.")
        firstname = Enterfirst_name() #Another input
    elif (firstname== " "): #if the first name is null
        print("\n First name must no be null. Try again.")
        firstname = Enterfirst_name() #Another input
    return firstname #returns First name if the input is valid.

def Entermiddleinit(): #Function that adds middle initial
    middleinit = input("\nEnter middle initial (Maximum of 2 characters): ") #Input from the user
    if (len(middleinit)>2): #length of the middle initial
        print("\n Middle initial exceeds the amount of character needed. Try again.")
        middleinit = Entermiddleinit() #Another input
    elif (middleinit== " "): #if the middle initial is null
        print("\n Friend name must no be null. Try again.")
        middleinit = Entermiddleinit() #Another input
    return middleinit #returns middle initial if the input is valid.

def Enterlastname(): #Function that adds last name
    lastname = input("\nEnter last name (Maximum of 25 characters): ") #Input from the user
    if (len(lastname)>25): #length of the last name
        print("\n last name exceeds the amount of character needed. Try again.")
        lastname = Enterlastname() #Another input
    elif (lastname== " "): #if the last name is null
        print("\n last name name must no be null. Try again.")
        lastname = Entermiddleinit() #Another input
    return lastname #returns last name if the input is valid.

def EnterEmail(): #Function that adds email address
    email = input("\nEnter email (Maximum of 50 characters): ") #Input from the user
    if (len(email)>50): #length of the email address
        print("\n email exceeds the amount of character needed. Try again.")
        email = EnterEmail() #Another input
    elif (email== " "): #if the email address is null
        print("\n email address must no be null. Try again.")
        email = EnterEmail() #Another input
    return email #returns friend name if the input is valid.

def Enteruserid():
    mycursor = database.cursor()
    sql_command = "SELECT * FROM user;"
    mycursor.execute(sql_command)
    myresult=mycursor.fetchall()

    try:
        mycursor=database.cursor()
        sql_command = "SELECT MAX(user_id) AS 'maximum' from user;"
        mycursor.execute(sql_command)
        myresult= mycursor.fetchone()
        myresult=myresult[0]
        myresult=myresult+1
        return myresult
    except:
        return 1

def AddFriend():
    print("=========Add a Friend=========") 
    userID=Enteruserid()
    firstname=Enterfirst_name()
    middleinit= Entermiddleinit()
    lastname=Enterlastname()
    email=EnterEmail()
    
    sql_cmd= "INSERT INTO user (user_id, first_name, middle_initial, last_name, email_address) VALUES (%s, %s, %s, %s, %s)"
    query_vals = (userID, firstname, middleinit, lastname, email)
    cursor.execute(sql_cmd, query_vals)
    database.commit()
    print("========Successfully added user===========")
    
def PrintFriend():
    mycursor = database.cursor() #execute sql query
    sql_command = "SELECT * FROM user;"
    mycursor.execute(sql_command)
    myresult = mycursor.fetchall()
    if myresult == None:
        print("\n No available data")
        AddFriend()
    else:
        arrayFriend = [] 
        print("\n The following are the friends added")
        for row in myresult:
            print("["+str(row[0])+"]", row[1])
            arrayFriend.append(row[0])

        while(True):
            try:
                userID= int(input("\nEnter the userID of the friend to update"))   
                if userID in arrayFriend:
                    return userID
                else:
                    print("\nThe user_id does not exist in the database")
            except ValueError:
                print("\nInvalid user id. Please try again")

def DeleteFriend():
    print("\n=======Delete a Friend=======")
    user_id= PrintFriend()
    mycursor = database.cursor()
    sql_command =  "DELETE FROM user WHERE user_id= %s"
    query_vals= (user_id,)
    mycursor.execute(sql_command,query_vals)
    result=mycursor.fetchone()
    if result==None:
        mycursor=database.cursor()
        sql_command="DELETE FROM user WHERE user_id=%s"
        query_vals=(user_id,)
        mycursor.execute(sql_command, query_vals)
        database.commit()
        print("\nSuccessfully deleted friend")
    else:
        print("\n The friend cannot be deleted because they have a running transaction")
        return

def SearchFriend():
    print("\n=======Search a Friend=======")
    friendname=input("Enter friend's name you want to search: ")
    cursor.execute("SELECT * FROM user WHERE first_name=%s", (friendname,))
    result = cursor.fetchall()

    if len(result)>0:
        print("Friend found.")
        for row in result:
            print("\n===========================")
            print("User ID: ", (row[0]))
            print("First Name: ", (row[1]))
            print("Middle Initial: ", (row[2]))
            print("Last Name: ", row[3])  
            print("Email address: ", row[4]) 
            print("=============================")  
            print("\n")   

    else:
        print("\n Friend Not Found. Try Again!")

def UpdateFriend():
    print("\n=======Update a Friend=======")
    user_id = PrintFriend()
    mycursor = database.cursor()
    command = "SELECT * FROM user WHERE user_id=%s"
    query_vals=(user_id,)
    mycursor.execute(command,query_vals)
    result=mycursor.fetchone()
    print("\n====================")
    print("User ID: ", result[0])
    print("First Name: ", result[1])
    print("Middle Initial: ", result[2])
    print("Last Name: ", result[3])
    print("Email address: ", result[4])

    print("Select the field you want to update: ")
    print("1. First name: ")
    print("2. Middle name: ")
    print("3. Last name: ")
    print("4. Email address: ")

    while(True):
        choice=int(input("\n Update a Friend"))
        try:
            if choice in range(1,6):
                if choice==1:
                    print("\n The current first name is: ", result[1])
                    print("\nUpdate the first name as: ")
                    newchoice=Enterfirst_name()
                    sqlcmd= "UPDATE user SET first_name=%s WHERE user_id=%s "

                    query_vals=(newchoice, user_id)
                    mycursor.execute(sqlcmd, query_vals)
                    database.commit()
                    print("\n Successfully updated first name")
                    return
                elif choice==2:
                    print("\n The current middle initial is: ", result[2])
                    print("\nUpdate the middle initial name as: ")
                    newchoice=Entermiddleinit()
                    sqlcmd= "UPDATE user SET middle_initial=%s WHERE user_id=%s "

                    query_vals=(newchoice, user_id)
                    mycursor.execute(sqlcmd, query_vals)
                    database.commit()
                    print("\n Successfully updated middle initial")
                    return
                elif choice==3:
                    print("\n The current last name is: ", result[3])
                    print("\nUpdate the last name as: ")
                    newchoice=Enterlastname()
                    sqlcmd= "UPDATE user SET last_name=%s WHERE user_id=%s "

                    query_vals=(newchoice, user_id)
                    mycursor.execute(sqlcmd, query_vals)
                    database.commit()
                    print("\n Successfully updated last name")
                    return
                
                elif choice==4:
                    print("\n The current email address is: ", result[4])
                    print("\nUpdate the email as: ")
                    newchoice=EnterEmail()
                    sqlcmd= "UPDATE user SET email_address=%s WHERE user_id=%s "

                    query_vals=(newchoice, user_id)
                    mycursor.execute(sqlcmd, query_vals)
                    database.commit()
                    print("\n Successfully updated email")
                    return
                
            else:
                print("\n Invalid input")

        except ValueError:
            print("\n Invalid input")    

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
        AddGroup()
    elif choice == "2":
        DeleteGroup()
    elif choice == "3":
        SearchGroup()
    elif choice == "4":
        UpdateGroup()
    elif choice == "0":
        main_menu()
    else:
        print("Invalid choice. Please try again.\n")

def Entergroupid():
    mycursor = database.cursor()
    sql_command = "SELECT * FROM groups;"
    mycursor.execute(sql_command)
    myresult=mycursor.fetchall()

    try:
        mycursor=database.cursor()
        sql_command = "SELECT MAX(group_id) AS 'maximum' from groups;"
        mycursor.execute(sql_command)
        myresult= mycursor.fetchone()
        myresult=myresult[0]
        myresult=myresult+1
        return myresult
    except:
        return 1

def Entergroup_name():
    groupname = input("\nEnter group name (Maximum of 25 characters): ") #Input from the user
    if (len(groupname)>30): #length of the group name
        print("\n First name exceeds the amount of character needed. Try again.")
        groupname = Entergroup_name() #Another input
    elif (groupname== " "): #if the group name is null
        print("\n Group name must not be null. Try again.")
        groupname = Entergroup_name() #Another input
    return groupname #returns group name if the input is valid.
  

def Enterno_of_group_members():
    while True:
        try:
            noofgroupmembers = int(input("\nEnter number of group members (integer from 2 to 999): "))
            if noofgroupmembers < 2 or noofgroupmembers > 999:
                raise ValueError
            return noofgroupmembers
            break
        except ValueError:
            print("Invalid input. Please enter an integer from 2 to 999.") 


###add group members
def AddGroup():
    print("=========Add a Group=========") 
    groupID=Entergroupid()
    groupname=Entergroup_name()
    noofgroupmembers= Enterno_of_group_members() 
    sql_cmd= "INSERT INTO groups (group_id, group_name, no_of_group_members) VALUES (%s, %s, %s)"
    query_vals = (groupID, groupname, noofgroupmembers)
    cursor.execute(sql_cmd, query_vals)
    database.commit()
    print("========Successfully added group===========")
    print("\n")
    print("\n")


def PrintGroup():
    mycursor = database.cursor() #execute sql query
    sql_command = "SELECT * FROM groups;"
    mycursor.execute(sql_command)
    myresult = mycursor.fetchall()
    if myresult == None:
        print("\n No available data")
        AddGroup()
    else:
        arrayGroup = [] 
        print("\n The following are the groups added:")
        for row in myresult:
            print("["+str(row[0])+"]", row[1])
            arrayGroup.append(row[0])

        while(True):
            try:
                groupID= int(input("\nEnter the groupID of the friend to update or delete: "))   
                if groupID in arrayGroup:
                    return groupID
                else:
                    print("\nThe group id does not exist in the database. Please try again.")
            except ValueError:
                print("\nInvalid group id. Please try again")


def DeleteGroup():
    print("\n=======Delete a Group=======")
    print("=========Delete a Group=========")
    group_id = input("Enter the group ID to delete: ")
    sql_command = "DELETE FROM groups WHERE group_id = %s"
    query_vals = (group_id,)
    cursor.execute(sql_command, query_vals)
    database.commit()
    print("Group deleted successfully!\n")
    '''
    group_id= PrintGroup()
    mycursor = database.cursor()
    sql_command =  "DELETE FROM groups WHERE group_id= %s"
    sql_command2 =  "DELETE FROM group_members WHERE group_id= %s"
    query_vals= (group_id,)
    mycursor.execute(sql_command, sql_command2, query_vals)
    result=mycursor.fetchone()
    if result==None:
        mycursor=database.cursor()
        sql_command="DELETE FROM groups WHERE group_id=%s"
        sql_command2 =  "DELETE FROM group_members WHERE group_id= %s"
        query_vals=(group_id,)
        mycursor.execute(sql_command, sql_command2, query_vals)
        database.commit()
        print("\nSuccessfully deleted group")
    else:
        print("\n The group cannot be deleted because they have a running transaction")
        return
    '''

def SearchGroup():
    print("\n=======Search a Group=======")
    group_name = input("Enter group name you want to search: ")
    cursor.execute("SELECT * FROM groups WHERE group_name=%s", (group_name,))
    result=cursor.fetchall()

    if len(result)>0:
        print("Group found.")
        for row in result:
            print("\n=========================")
            print("Group ID: ",(row[0]))
            print("Group name: ",(row[1]))
            print("Number of group members: ",(row[2]))
            print("=========================")
            print("\n")
            print("\n")
    else: 
        print("\n Group not found. Please try again.")


def UpdateGroup():
    print("\n=======Update a Group=======")
    group_id = input("Enter group id you want to update: ")
    group_name = input("Enter updated group name: ")
    no_of_group_members = input("Enter updated number of group members: ")
    cursor.execute("UPDATE groups SET group_name = %s, no_of_group_members = %s WHERE group_id = %s", (group_name, no_of_group_members, group_id))
    database.commit()

    print("Group updated successfully!\n")

def payment():
    print("------------------------------------------------")
    print("   What would you like to do with a payment? ")
    print("------------------------------------------------")
    print("[1] Settle Payment")
    print("[0] Back to main menu")
    print("------------------------------------------------")
    choice = input("Please enter your choice: ")
    print("\n")

    if choice == "1":
        print("------------------------------------------------")
        print("                   Payment")
        print("------------------------------------------------")
        user_id = input("Enter the friend's ID: ")
        payment_amount = float(input("Enter the payment amount: "))

        # Get the current total_amount for the friend
        cursor.execute("SELECT total_amount FROM expense WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()

        if result:
            total_amount = float(result[0])

            # Check if the payment amount is valid
            if payment_amount <= total_amount:
                new_total_amount = total_amount - payment_amount

                # Update the total_amount in the database
                cursor.execute("UPDATE expense SET total_amount = %s WHERE user_id = %s", (new_total_amount, user_id))
                database.commit()

                print(f"Payment of {payment_amount} successfully deducted from friend's total_amount.")
            else:
                print("Invalid payment amount. The payment amount exceeds the friend's total_amount.")
        else:
            print("Friend not found.")
    
    elif choice == "0":
        main_menu()

def reports():
    print("------------------------------------------------")
    print("    What  report would you like to generate? ")
    print("------------------------------------------------")
    print("[1] View all expenses made within a month")
    print("[2] View all expenses made with a friend")
    print("[3] View all expenses made with a group")
    print("[4] View current balance from all expenses")
    print("[5] View all expense with outstanding balance")
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
        group_id = input("Enter the group ID: ")
        print("\n")
        sql_command = "SELECT * FROM expense WHERE group_id = %s"
        cursor.execute(sql_command, (group_id,))
        expenses = cursor.fetchall()

        if len(expenses) > 0 and len(expenses) < 2:
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

    elif choice == "3":
        group_id = input("Enter the group ID: ")
        print("\n")
        sql_command2 = "SELECT * FROM expense WHERE group_id = %s"
        cursor.execute(sql_command2, (group_id,))
        expenses = cursor.fetchall()

        if len(expenses) >= 2:
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
        sql_command4 = "SELECT SUM(total_amount) AS 'Current Balance from All Expenses' FROM expense WHERE is_settled = 'No'"
        cursor.execute(sql_command4)
        result = cursor.fetchone()
        if result[0] is not None:
            print("Current Balance from All Expenses: $", result[0])
        else:
            print("No expenses with 'No' settlement found.")
        
    elif choice == "5":
        sql_command5 = "SELECT * FROM groups NATURAL JOIN expense WHERE is_settled='No'"
        cursor.execute(sql_command5)
        result = cursor.fetchall()

        if len(result) > 0: 
            print("expense with outstanding balance:")
            for row in result:
                print(f"Friend: {row[5]}")
                print(f"Expense ID: {row[3]}")
                print(f"Group ID: {row[0]}")
                print(f"Date Incurred: {row[4]}")
                print(f"Total Amount: {row[7]}")
                print("--------------------")
        else:
            print("No expense with outstanding balance found.")

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