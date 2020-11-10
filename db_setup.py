import sqlite3
import datetime

con = sqlite3.connect('restaraunt_1.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Reservations(Name TEXT, PartyCount INTEGER, Date timestamp, Time TIME, Total REAL)')

cur.execute('CREATE TABLE IF NOT EXISTS Menu(Name TEXT, Price REAL)')
cur.execute(''''INSERT INTO Menu VALUES
    ('Crispy Asparagus', $7.49)
    ('Regular Spicy and Loaded Boneless Wings' $10.99)
    ('White Spinach Queso' $7.99)
    ('Crispy Cheddar Bites' $7.49)
    ('Fried Pickles' $7.49)
    ('Triple Dipper Combination of 3 appetizers' $12.99)
    ('Chips & Salsa' $5.29)
    ('Texas Cheese Fries Full' $9.49)
    ('Classic Nachos' $9.99)
    ('Classic Nachos with Fajita Chicken or Beef' $11.99)
    ('Fresh Guacamole' $7.49)
    ('Signature Wings' $10.49)
    ('Signature Boneless Wings' $10.69)
    ('House Salad' $4.99)
    ('Quesadilla Explosion Salad' $10.99)
    ('Santa Fe Chicken Salad' $10.99)
    ('Boneless Buffalo Chicken Salad' $10.99)
    ('Caribbean Salad with Grilled Chicken' $10.99)
    ('Caribbean Salad with Grilled Shrimp' $11.99)
    ('Grilled Chicken Salad' $10.99)
    ('Soup and House Salad' $6.99)
    ('Bacon Avocado Chicken Sandwhich' $10.49)
    ('Buffalo Chicken Ranch Sandwhich' $9.99)
    ('Southern Smokehouse Burger' $10.99)
    ('Big Mouth Bites' )

)

cur.execute('CREATE TABLE IF NOT EXISTS Carryout(Name TEXT, Total REAL)')

cur.execute('CREATE TABLE IF NOT EXISTS Delivery(Name TEXT, Destination TEXT, Total REAL)')

cur.execute('CREATE TABLE IF NOT EXISTS Availability(Available INTEGER)')

con.commit()