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
    for phones in results:
        print(f"{phones[1]}{phones[2]}{phones[3]}{phones[4]}")
    #loop finishes
    db.close()



#main code for db
print_all_phonesgb()
