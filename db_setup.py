import sqlite3
import datetime

con = sqlite3.connect('resteraunt_1.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Reservations(Name TEXT, Party-Count INTEGER, Date timestamp, Order REAL)')

cur.execute('CREATE TABLE IF NOT EXISTS Menu(Name TEXT, Item REAL')