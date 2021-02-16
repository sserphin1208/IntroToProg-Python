# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What): sserphin, 12Feb2020, Created the script
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

objFile = open("ToDoList.txt", "w")
objFile.write("Dust the TV, low" + '\n')
objFile.close()

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(", ")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("TODO List")
        for dicRow in lstTable:
            print(dicRow["Task"] + ', ' + dicRow["Priority"].strip())
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Please enter a TODO item: ")
        strPriority = input("Please enter its' priority: ")
        strData = [strTask, strPriority]
        dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        lstTable.remove(dicRow)
        print("The last todo was removed!")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "a")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
        objFile.close()
        print("Data saved")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("good bye!")
        break
    else:
        print('That is not a valid option, please choose (1-5)')
        input("Press enter to continue")
