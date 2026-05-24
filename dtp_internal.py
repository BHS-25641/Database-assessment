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


# function 2 - gb amount starting from highest
def print_all_phonesgb_by_gb_desc():
    '''print all the phones sorted by highest gb '''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from phonesgb ORDER BY gb_amount DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    # loop through all the results
    print("name                     amount of gb   manufacturer     ranking ")
    for phones in results:
        print(f"{phones[1]:<30}{phones[2]:<10}{phones[3]:<20}{phones[4]:<25}")
    # loop finishes
    db.close()


# function 3 - gb amount starting from lowest
def print_all_phones_by_gb_asc():
    '''print all the phones sorted by lowest gb '''
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


# function 4 - select all manufacturers
def print_all_phones_manufacturers():
    '''print all the phones by manufacturer '''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT manufacturer from phonesgb;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("manufacturer ")
    for phones in results:
        print(f"{phones[0]:<30}")
    # loop finishes
    db.close()


# function 5 - print all apple phones and data 
def print_all_applephones_data():
    '''print all apple phones and data'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from phonesgb WHERE manufacturer = 'apple';";
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                     amount of gb   manufacturer     ranking ")
    for phones in results:
        print(f"{phones[1]:<30}{phones[2]:<10}{phones[3]:<20}{phones[4]:<25}")
    # loop finishes
    db.close()


# function 6 - print top 5 phones
def print_all_top_phones():
    '''print phones that have ranking above 5'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from phonesgb WHERE ranking > 5;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                     amount of gb   manufacturer     ranking ")
    for phones in results:
        print(f"{phones[1]:<30}{phones[2]:<10}{phones[3]:<20}{phones[4]:<25}")
    # loop finishes
    db.close()


# web application menu/ menu interface
while True:
    menu = print("""Welcome to my database application.
                This is all about how much gb is within phones""")
    user_input = input(
        """
        Which of the following options would you like to pick. Press any number from 1-7.
        1. Print all phones
        2. Print all phones by highest gb
        3. Print all phones by lowest gb
        4. Print all phone manufacturers
        5. Print all apple manufacturers
        6. Print all samsung manufacturers
        7. Exit
        """)
    if user_input == "1":
        print_all_phonesgb()
    elif user_input == "2":
        print_all_phonesgb_by_gb_desc()
    elif user_input == "3":
        print_all_phones_by_gb_asc()
    elif user_input == "4":
        print_all_phones_manufacturers()
    elif user_input == "5":
        print_all_applephones_data()
    elif user_input == "6":
        print_all_top_phones()
    elif user_input == "7":
        print("Goodbye!")
        break
    else:
        print("That was not an option\n")
