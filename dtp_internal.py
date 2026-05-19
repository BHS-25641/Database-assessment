# docstring phones databse application
# import sqilte3 into vs code

import sqlite3

# variables to prevent magic numbers
DATABASE = "phonesgb.db"


# functions
# function 1 - print all phones 
def print_all_phonesgb():
    '''print all the phones nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from phonesgb;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                     amount of gb   manufacturer     ranking ")
    for phones in results:
        print(f"{phones[1]:<30}{phones[2]:<10}{phones[3]:<20}{phones[4]:<25}")
    # loop finishes
    db.close()


#function 2 - gb amount starting from highest
def print_all_phonesgb_by_gb_desc():
    '''print all the phones sorted by highest gb '''
db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT * from phonesgb ORDER BY gb_amount;"
cursor.execute(sql)
results = cursor.fetchall()
# loop through all the results
print("name                     amount of gb   manufacturer     ranking ")
for phones in results:
    print(f"{phones[1]:<30}{phones[2]:<10}{phones[3]:<20}{phones[4]:<25}")
# loop finishes
db.close()
  


# web application menu
while True:
    menu = print("""Welcome to my database application.
                This is all about how much of gb within phones""")
    user_input = input("\nWhat would you like to see.\n1. Print all aircraft\n5.Exit\n")
    if user_input == "1":
        print_all_phonesgb()
    elif user_input == "2":
        print_all_phonesgb_by_gb_desc()
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        break
    else:
        print("That was not an option\n")