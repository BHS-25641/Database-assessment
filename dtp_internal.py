#docstring phones databse application
#import sqilte3 into vs code

import sqlite3

#variables to prevent magic numbers
DATABASE = "phonesgb.db"



#functions
def print_all_phonesgb():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from phonesgb;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                     amount of gb   manufacturer     ranking ")
    for phones in results:
        print(f"{phones[1]:<30}{phones[2]:<10}{phones[3]:<20}{phones[4]:<25}")
    #loop finishes
    db.close()



#main code for db
print_all_phonesgb()
