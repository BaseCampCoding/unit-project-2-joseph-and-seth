import sqlite3
import datetime

con = sqlite3.connect('restaraunt_1.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Reservations(Name TEXT, Party-Count INTEGER, Date timestamp, Time TIME, Total REAL)')

cur.execute('CREATE TABLE IF NOT EXISTS Menu(Name TEXT, Price REAL)')

cur.execute('CREATE TABLE IF NOT EXISTS Carry-out(Name TEXT, Total REAL)')

cur.execute('CREATE TABLE IF NOT EXISTS Delivery(Name TEXT, Destination TEXT, Total REAL)')

cur.execute('CREATE TABLE IF NOT EXISTS Availability(Available INTEGER)')

con.commit()