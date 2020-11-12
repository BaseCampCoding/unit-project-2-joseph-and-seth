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

outbacksh_list = [
    (0, "Bloomin' Onion", 8.99),
    (1, "Aussie Cheese Fries Regular", 10.49),
    (2, "Aussie Cheese Fries Small", 8.49),
    (3, "Wings (Mild, Medium, Hot", 10.99),
    (4, "Alice Springs Chicken Quesadillas", 10.49),
    (5, "Seared Peppered Ahi", 12.49),
    (6, "Wood-fire Grilled Shrimp on the Barbie", 10.49),
    (7, "Coconut Shrimp", 9.99),
    (8, "Aussie Signature Sampler", 11.99),
    (9, "Bloom Petals", 4.49),
    (10, "Alice Springs Chicken Quesadillas (Small)", 7.49),
    (11, "Coconut Shrimp Small", 4.99),
    (12, "Seared Peppered Ahi Small", 9.49),
    (13, "Baked Potato Soup Cup", 4.49),
    (14, "Baked Potato Soup Bowl", 5.99),
    (15, "Chicken Tortilla Soup Cup", 4.49),
    (16, "Chicken Tortilla Soup Bowl", 5.99),
    (17, "French Onion Soup", 6.99),
    (18, "Aussie Cobb Salad", 10.99),
    (19, "Aussie Cobb Salad with chicken", 13.99),
    (20, "Steakhouse Salad", 13.99),
    (21, "Caesar Salad", 9.99),
    (22, "Caesar Salad with chicken or shrimp", 12.99),
    (23, "House Side Salad", 4.99),
    (24, "Caesar Side Salad", 4.99),
    (25, "Blue Cheese Wedge Side Salad", 5.99),
    (26, "Blue Cheese Pecan Chopped Side Salad", 5.99),
    (27, "Victoria's Filet Mignon 6oz", 22.99),
    (28, "Victoria's Filet Mignon 9oz", 27.99),
    (29, "New York Strip 14oz", 24.49),
    (30, "Outback Center-cut Sirloin 6oz", 13.29),
    (31, "Outback Center-cut Sirloin 8oz", 17.29),
    (32, "Outback Center-cut Sirloin 11oz", 20.29),
    (33, "T-Bone 22oz", 28.49),
    (34, "Ribeye 10oz", 20.99),
    (35, "Ribeye 14oz", 25.49),
    (36, "Bone-in Natural Cut Ribeye", 28.99),
    (37, "Slow-Roasted Prime Rib 8oz", 19.49),
    (38, "Slow-Roasted Prime Rib 12oz", 22.49),
    (39, "Slow-Roasted Prime Rib 16oz", 24.49),
    (40, "Sirloin & Choice of Shrimp 8oz", 20.29),
    (41, "Sirloin & Choice of Shrimp 11oz", 22.29),
    (42, "Classic Tendrloin 9.75oz", 11.99),
    (43, "Classic Tenderloin 13oz", 14.99),
    (44, "Roasted Garlic Butter Style", 1.49),
    (45, "Mushroom Marsala Style", 1.99),
    (46, "Grilled Shrimp", 5.99),
    (47, "Coconut Shrimp", 5.99),
    (48, "Jumbo Lump Crab Cake", 7.99),
    (49, "Grilled Lobster Tail", 10.99),
    (50, "Steamed Lobster Tail", 10.99),
    (51, "Aussie Steak Tacos", 10.99),
    (52, "Aussie Fish Tacos", 11.99),
    (53, "Aussie Chicken Tacos", 10.99),
    (54, "The Bloomin' Burger", 10.49),
    (55, "The Outback Burger", 9.49),
    (56, "Grass-Fed Burger with Aged Cheddar", 12.49),
    (57, "Double Burger", 11.49),
    (58, "Crispy Chicken Sandwich", 10.99),
    (59, "Bacon-Bourbon Salmon 7oz", 16.99),
    (60, "Bacon-Bourbon Salmon 10oz", 18.99),
    (61, "Perfectly Grilled Salmon 7oz", 15.99),
    (62, "Perfectly Grilled Salmon 10oz", 17.99),
    (63, "Tilapia with Pure Lump Crab Meat", 16.99),
    (64, "Hand-Breaded Shrimp", 14.99),
    (65, "Crab Cakes", 19.99),
    (66, "Lobster Tails", 26.49),
    (67, "Parmesan-Herb Crusted Chicken", 14.99),
    (68, "Grilled Chicken on the Barbie", 13.99),
    (69, "Alice Springs Chicken", 15.99),
    (70, "Chicken Tender Platter", 12.99),
    (71, "Baby Back Ribs Full Order", 21.49),
    (72, "Baby Back Ribs Half Order", 16.99),
    (73, "Pork Porterhouse", 14.99),
    (74, "New Zealand Lamb", 22.49),
    (75, "Homestyle Mashed Potatoes, Aussie Fries, Baked Potato, & Sweet Potato", 2.99),
    (76, "Fresh Seasonal Mixed Veggies, Fresh Steamed Broccoli, & Sauteed Mushrooms", 2.99),
    (77, "Baked Potato & Chicken Tortilla Soup Cup", 4.49),
    (78, "Steakhouse Mac & Cheese", 4.99),
    (79, "Broccoli & Cheese", 3.99),
    (80, "Loaded Mashed Potatoes", 3.99),
    (81, "Grilled Asparagus", 3.99),
    (82, "Chocolate Thunder from Down Under", 7.99),
    (83, "New York-Style Cheesecake", 6.99),
    (84, "Salted Caramel Topped Cheesecake", 7.99),
    (85, "Triple-Layer Carrot Cake", 6.99),
    (86, "Salted Caramel Cookie Skillet", 4.99),
    (87, "Double Chocolate or Seasonal Parfaits", 4.99),

]


reservation_times = [
    ("11/11/2020", "8:00 p.m."),
    ("11/11/2020", "5:00 p.m"),
    ("11/14/2020", "3:30 p.m"),
    ("11/14/2020", "6:30 p.m."),
    ("11/15/2020", "9:00 p.m."),
    ("11/16/2020", "4:00 p.m."),
    ("11/20/2020", "6:30 p.m."),
    ("11/21/2020", "12:00 p.m."),
    ("11/24/2020", "1:00 p.m."),
    ("11/30/2020", "11:00 p.m."),
]

con = sqlite3.connect("restaraunt_1.db")
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS Reservations(Name TEXT, PartyCount INTEGER, Date timestamp, Time TIME, Items TEXT, Total REAL)"
)

cur.execute("CREATE TABLE IF NOT EXISTS ReservationTimes(Date timestamp, Time TIME)")
for row in reservation_times:
    cur.execute("INSERT INTO ReservationTimes VALUES (?, ?)", row)

cur.execute("CREATE TABLE IF NOT EXISTS Menu(ID INTEGER, Item TEXT, Price REAL)")
for row in chilis_list:
    cur.execute("INSERT INTO Menu VALUES (?, ?, ?)", row)

cur.execute(
    "CREATE TABLE IF NOT EXISTS Carryout(Name TEXT, Time TIME, Items TEXT, Total REAL)"
)

cur.execute(
    "CREATE TABLE IF NOT EXISTS Delivery(Name TEXT, Destination TEXT, DeliveryTime TIME, Items TEXT, Total REAL)"
)

cur.execute("CREATE TABLE IF NOT EXISTS Availability(Available INTEGER)")

con.commit()
con.close()


con = sqlite3.connect('restaurant_2.db')
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS Reservations(Name TEXT, PartyCount INTEGER, Date timestamp, Time TIME, Items TEXT, Total REAL)"
)

cur.execute("CREATE TABLE IF NOT EXISTS ReservationTimes(Date timestamp, Time TIME)")
for row in reservation_times:
    cur.execute("INSERT INTO ReservationTimes VALUES (?, ?)", row)

cur.execute("CREATE TABLE IF NOT EXISTS Menu(ID INTEGER, Item TEXT, Price REAL)")
for row in outbacksh_list:
    cur.execute("INSERT INTO Menu VALUES (?, ?, ?)", row)

cur.execute(
    "CREATE TABLE IF NOT EXISTS Carryout(Name TEXT, Time TIME, Items TEXT, Total REAL)"
)

cur.execute(
    "CREATE TABLE IF NOT EXISTS Delivery(Name TEXT, Destination TEXT, DeliveryTime TIME, Items TEXT, Total REAL)"
)

cur.execute("CREATE TABLE IF NOT EXISTS Availability(Available INTEGER)")
con.commit()
con.close()