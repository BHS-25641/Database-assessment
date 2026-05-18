#import sqilte3 into vs code

import sqlite3

#variables to prevent magic numbers
DATABASE = "phonesgb.db"



#functions




#main code for db
db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT * from phonesgb;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
