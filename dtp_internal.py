import sqlite3
db = sqlite3.connect("phonesgb.db")
cursor = db.cursor()

db.close()
