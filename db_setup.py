import sqlite3
import datetime

chilis_list = [
    (0, "Crispy Asparagus", 7.49),
    (1, "Regular Spicy and Loaded Boneless Wings", 10.99),
    (2, "White Spinach Queso", 7.99),
    (3, "Crispy Cheddar Bites", 7.49),
    (4, "Fried Pickles", 7.49),
    (5, "Triple Dipper Combination of 3 appetizers", 12.99),
    (6, "Chips & Salsa", 5.29),
    (7, "Texas Cheese Fries Full", 9.49),
    (8, "Classic Nachos", 9.99),
    (9, "Classic Nachos with Fajita Chicken or Beef", 11.99),
    (10, "Fresh Guacamole", 7.49),
    (11, "Signature Wings", 10.49),
    (12, "Signature Boneless Wings", 10.69),
    (13, "House Salad", 4.99),
    (14, "Quesadilla Explosion Salad", 10.99),
    (15, "Santa Fe Chicken Salad", 10.99),
    (16, "Boneless Buffalo Chicken Salad", 10.99),
    (17, "Caribbean Salad with Grilled Chicken", 10.99),
    (18, "Caribbean Salad with Grilled Shrimp", 11.99),
    (19, "Grilled Chicken Salad", 10.99),
    (20, "Soup and House Salad", 6.99),
    (21, "Bacon Avocado Chicken Sandwhich", 10.49),
    (22, "Buffalo Chicken Ranch Sandwhich", 9.99),
    (23, "Southern Smokehouse Burger", 10.99),
    (24, "Big Mouth Bites", 9.59),
    (25, "Ancho Salmon", 14.99),
    (26, "6 oz Sirloin with Grilled Avocado", 10.99),
    (27, "Mango Chile Chicken", 11.49),
    (28, "Grilled Chicken Salad", 10.99),
    (29, "Margarita Grilled Chicken", 10.99),
    (30, "Mix and Match Fajitas", 12.99),
    (31, "Mix and Match Fajita Trio", 16.99),
    (32, "Beef Enchiladas", 11.49),
    (33, "Green Chile Chicken Enchiladas", 11.49),
    (34, "Prime Rib Fresh Mex Bowl", 10.99),
    (35, "Chipotle Chicken Fresh Mex Bowl", 11.49),
    (36, "Smothered Prime Rib Burrito", 10.99),
    (37, "Cajun Chicken Pasta", 11.99),
    (38, "Crispy Honey-Chipotle Crispers", 11.29),
    (39, "Original Chicken Crispers", 11.29),
    (40, "Lunch Combo - Fajitas", 9.00),
    (41, "Lunch Combo - Big Mouth Bites", 7.49),
    (42, "Lunch Combo - Chipotle Chicken Fresh Mex Bowl", 8.00),
    (43, "Dips", 0.79),
    (44, "Molten Chocolate Cake", 7.29),
    (45, "Skillet Chocolate Chip Cookie", 7.29),
    (46, "Cheesecake", 7.29),
    (47, "Fountain Drinks 32 oz", 1.00),
    (48, "Blackberry Iced Tea", 2.79),
    (49, "Mango Iced Tea", 2.79),
    (50, "Strawberry Lemonade", 2.99),
    (51, "IBC Rootbeer", 2.49),
    (52, "Dasani", 2.09),
    (53, "Coffee", 2.29),
    (54, "Milk", 2.29),
    (55, "Iced Tea (Gallon)", 5.89),
    (56, "Strawberry Lemonade (Gallon)", 7.99),
    (57, "Arnold Palmer", 2.59),
    (58, "Juice", 2.19),
    (59, "Pizza Pepperoni", 4.99),
    (60, "Mac & Cheese", 4.99),
    (61, "Pepper Pals Grilled Cheese Sandwich", 4.99),
    (62, "Pepper Pals Cheese Quesadilla", 4.99),
    (63, "Pepper Pals Crispy Chicken Crispers", 4.99),
    (64, "Pepper Pals Grilled Chicken Bites", 4.99),
    (65, "Pepper Pals Cheese Burger Bites", 4.99),
]

reservation_times = [
    ('11/11/2020', '8:00 p.m.'),
    ('11/11/2020', '5:00 p.m'),
    ('11/14/2020', '3:30 p.m'),
    ('11/14/2020', '6:30 p.m.'),
    ('11/15/2020', '9:00 p.m.'),
    ('11/16/2020', '4:00 p.m.'),
    ('11/20/2020', '6:30 p.m.'),
    ('11/21/2020', '12:00 p.m.'),
    ('11/24/2020', '1:00 p.m.'),
    ('11/30/2020', '11:00 p.m.'),
]

con = sqlite3.connect("restaraunt_1.db")
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS Reservations(Name TEXT, PartyCount INTEGER, Date timestamp, Time TIME, Total REAL)"
)

cur.execute("CREATE TABLE IF NOT EXISTS ReservationTimes(Date timestamp, Time TIME)")
for row in reservation_times:
    cur.execute("INSERT INTO ReservationTimes VALUES (?, ?)", row)

cur.execute("CREATE TABLE IF NOT EXISTS Menu(ID INTEGER, Item TEXT, Price REAL)")
for row in chilis_list:
    cur.execute("INSERT INTO Menu VALUES (?, ?, ?)", row)

cur.execute("CREATE TABLE IF NOT EXISTS Carryout(Name TEXT, Total REAL)")

cur.execute(
    "CREATE TABLE IF NOT EXISTS Delivery(Name TEXT, Destination TEXT, Total REAL)"
)

cur.execute("CREATE TABLE IF NOT EXISTS Availability(Available INTEGER)")

con.commit()