import sqlite3
import datetime

chilis_list = [
    (0, "Crispy Asparagus", 7.49, "Appetizer"),
    (1, "Regular Spicy and Loaded Boneless Wings", 10.99, "Appetizer"),
    (2, "White Spinach Queso", 7.99, "Appetizer"),
    (3, "Crispy Cheddar Bites", 7.49, "Appetizer"),
    (4, "Fried Pickles", 7.49, "Appetizer"),
    (5, "Triple Dipper Combination of 3 appetizers", 12.99, "Appetizer"),
    (6, "Chips & Salsa", 5.29, "Appetizer"),
    (7, "Texas Cheese Fries Full", 9.49, "Appetizer"),
    (8, "Classic Nachos", 9.99, "Appetizer"),
    (9, "Classic Nachos with Fajita Chicken or Beef", 11.99, "Appetizer"),
    (10, "Fresh Guacamole", 7.49, "Appetizer"),
    (11, "Signature Wings", 10.49, "Appetizer"),
    (12, "Signature Boneless Wings", 10.69, "Appetizer"),
    (13, "House Salad", 4.99, "Appetizer"),
    (14, "Quesadilla Explosion Salad", 10.99, "Salad"),
    (15, "Santa Fe Chicken Salad", 10.99, "Salad"),
    (16, "Boneless Buffalo Chicken Salad", 10.99, "Salad"),
    (17, "Caribbean Salad with Grilled Chicken", 10.99, "Salad"),
    (18, "Caribbean Salad with Grilled Shrimp", 11.99, "Salad"),
    (19, "Grilled Chicken Salad", 10.99, "Salad"),
    (20, "Soup and House Salad", 6.99, "Salad"),
    (21, "Bacon Avocado Chicken Sandwich", 10.49, "Sandwich"),
    (22, "Buffalo Chicken Ranch Sandwich", 9.99, "Sandwich"),
    (23, "Southern Smokehouse Burger", 10.99, "Sandwich"),
    (24, "Big Mouth Bites", 9.59, "Sandwich"),
    (25, "Ancho Salmon", 14.99, "Meat"),
    (26, "6 oz Sirloin with Grilled Avocado", 10.99, "Meat"),
    (27, "Mango Chile Chicken", 11.49, "Chicken"),
    (28, "Grilled Chicken Salad", 10.99, "Salad"),
    (29, "Margarita Grilled Chicken", 10.99, "Chicken"),
    (30, "Mix and Match Fajitas", 12.99, "Mexican"),
    (31, "Mix and Match Fajita Trio", 16.99, "Mexican"),
    (32, "Beef Enchiladas", 11.49, "Mexican"),
    (33, "Green Chile Chicken Enchiladas", 11.49, "Mexican"),
    (34, "Prime Rib Fresh Mex Bowl", 10.99, "Mexican"),
    (35, "Chipotle Chicken Fresh Mex Bowl", 11.49, "Mexican"),
    (36, "Smothered Prime Rib Burrito", 10.99, "Mexican"),
    (37, "Cajun Chicken Pasta", 11.99, "Chicken"),
    (38, "Crispy Honey-Chipotle Crispers", 11.29, "Chicken"),
    (39, "Original Chicken Crispers", 11.29, "Chicken"),
    (40, "Lunch Combo - Fajitas", 9.00, "Combo"),
    (41, "Lunch Combo - Big Mouth Bites", 7.49, "Combo"),
    (42, "Lunch Combo - Chipotle Chicken Fresh Mex Bowl", 8.00, "Combo"),
    (44, "Molten Chocolate Cake", 7.29, "Dessert"),
    (45, "Skillet Chocolate Chip Cookie", 7.29, "Dessert"),
    (46, "Cheesecake", 7.29, "Dessert"),
    (47, "Fountain Drinks 32 oz", 1.00, "Beverage"),
    (48, "Blackberry Iced Tea", 2.79, "Beverage"),
    (49, "Mango Iced Tea", 2.79, "Beverage"),
    (50, "Strawberry Lemonade", 2.99, "Beverage"),
    (51, "IBC Rootbeer", 2.49, "Beverage"),
    (52, "Dasani", 2.09, "Beverage"),
    (53, "Coffee", 2.29, "Beverage"),
    (54, "Milk", 2.29, "Beverage"),
    (55, "Iced Tea (Gallon)", 5.89, "Beverage"),
    (56, "Strawberry Lemonade (Gallon)", 7.99, "Beverage"),
    (57, "Arnold Palmer", 2.59, "Beverage"),
    (58, "Juice", 2.19, "Beverage"),
    (59, "Pizza Pepperoni", 4.99, "Sides"),
    (60, "Mac & Cheese", 4.99, "Sides"),
    (61, "Pepper Pals Grilled Cheese Sandwich", 4.99, "Kids Meals"),
    (62, "Pepper Pals Cheese Quesadilla", 4.99, "Kids Meals"),
    (63, "Pepper Pals Crispy Chicken Crispers", 4.99, "Kids Meals"),
    (64, "Pepper Pals Grilled Chicken Bites", 4.99, "Kids Meals"),
    (65, "Pepper Pals Cheese Burger Bites", 4.99, "Kids Meals"),
]

outbacksh_list = [
    (0, "Bloomin' Onion", 8.99, "Appetizer"),
    (1, "Aussie Cheese Fries Regular", 10.49, "Appetizer"),
    (2, "Aussie Cheese Fries Small", 8.49, "Appetizer"),
    (3, "Wings (Mild, Medium, Hot", 10.99, "Appetizer"),
    (4, "Alice Springs Chicken Quesadillas", 10.49, "Appetizer"),
    (5, "Seared Peppered Ahi", 12.49, "Appetizer"),
    (6, "Wood-fire Grilled Shrimp on the Barbie", 10.49, "Appetizer"),
    (7, "Coconut Shrimp", 9.99, "Appetizer"),
    (8, "Aussie Signature Sampler", 11.99, "Appetizer"),
    (9, "Bloom Petals", 4.49, "Appetizer"),
    (10, "Alice Springs Chicken Quesadillas (Small)", 7.49, "Appetizer"),
    (11, "Coconut Shrimp Small", 4.99, "Appetizer"),
    (12, "Seared Peppered Ahi Small", 9.49, "Appetizer"),
    (13, "Baked Potato Soup Cup", 4.49, "Soup"),
    (14, "Baked Potato Soup Bowl", 5.99, "Soup"),
    (15, "Chicken Tortilla Soup Cup", 4.49, "Soup"),
    (16, "Chicken Tortilla Soup Bowl", 5.99, "Soup"),
    (17, "French Onion Soup", 6.99, "Soup"),
    (18, "Aussie Cobb Salad", 10.99, "Salad"),
    (19, "Aussie Cobb Salad with chicken", 13.99, "Salad"),
    (20, "Steakhouse Salad", 13.99, "Salad"),
    (21, "Caesar Salad", 9.99, "Salad"),
    (22, "Caesar Salad with chicken or shrimp", 12.99, "Salad"),
    (23, "House Side Salad", 4.99, "Salad"),
    (24, "Caesar Side Salad", 4.99, "Salad"),
    (25, "Blue Cheese Wedge Side Salad", 5.99, "Salad"),
    (26, "Blue Cheese Pecan Chopped Side Salad", 5.99, "Salad"),
    (27, "Victoria's Filet Mignon 6oz", 22.99, "Steak"),
    (28, "Victoria's Filet Mignon 9oz", 27.99, "Steak"),
    (29, "New York Strip 14oz", 24.49, "Steak"),
    (30, "Outback Center-cut Sirloin 6oz", 13.29, "Steak"),
    (31, "Outback Center-cut Sirloin 8oz", 17.29, "Steak"),
    (32, "Outback Center-cut Sirloin 11oz", 20.29, "Steak"),
    (33, "T-Bone 22oz", 28.49, "Steak"),
    (34, "Ribeye 10oz", 20.99, "Steak"),
    (35, "Ribeye 14oz", 25.49, "Steak"),
    (36, "Bone-in Natural Cut Ribeye", 28.99, "Steak"),
    (37, "Slow-Roasted Prime Rib 8oz", 19.49, "Steak"),
    (38, "Slow-Roasted Prime Rib 12oz", 22.49, "Steak"),
    (39, "Slow-Roasted Prime Rib 16oz", 24.49, "Steak"),
    (40, "Sirloin & Choice of Shrimp 8oz", 20.29, "Steak"),
    (41, "Sirloin & Choice of Shrimp 11oz", 22.29, "Steak"),
    (42, "Classic Tenderloin 9.75oz", 11.99, "Steak"),
    (43, "Classic Tenderloin 13oz", 14.99, "Steak"),
    (44, "Roasted Garlic Butter Style", 1.49, "Nil"),
    (45, "Mushroom Marsala Style", 1.99, "Nil"),
    (46, "Grilled Shrimp", 5.99, "Seafood"),
    (47, "Coconut Shrimp", 5.99, "Seafood"),
    (48, "Jumbo Lump Crab Cake", 7.99, "Seafood"),
    (49, "Grilled Lobster Tail", 10.99, "Seafood"),
    (50, "Steamed Lobster Tail", 10.99, "Seafood"),
    (51, "Aussie Steak Tacos", 10.99, "Taco"),
    (52, "Aussie Fish Tacos", 11.99, "Taco"),
    (53, "Aussie Chicken Tacos", 10.99, "Taco"),
    (54, "The Bloomin' Burger", 10.49, "Sandwich"),
    (55, "The Outback Burger", 9.49, "Sandwich"),
    (56, "Grass-Fed Burger with Aged Cheddar", 12.49, "Sandwich"),
    (57, "Double Burger", 11.49, "Sandwich"),
    (58, "Crispy Chicken Sandwich", 10.99, "Sandwich"),
    (59, "Bacon-Bourbon Salmon 7oz", 16.99, "Seafood"),
    (60, "Bacon-Bourbon Salmon 10oz", 18.99, "Seafood"),
    (61, "Perfectly Grilled Salmon 7oz", 15.99, "Seafood"),
    (62, "Perfectly Grilled Salmon 10oz", 17.99, "Seafood"),
    (63, "Tilapia with Pure Lump Crab Meat", 16.99, "Seafood"),
    (64, "Hand-Breaded Shrimp", 14.99, "Seafood"),
    (65, "Crab Cakes", 19.99, "Seafood"),
    (66, "Lobster Tails", 26.49, "Seafood"),
    (67, "Parmesan-Herb Crusted Chicken", 14.99, "Chicken"),
    (68, "Grilled Chicken on the Barbie", 13.99, "Chicken"),
    (69, "Alice Springs Chicken", 15.99, "Chicken"),
    (70, "Chicken Tender Platter", 12.99, "Chicken"),
    (71, "Baby Back Ribs Full Order", 21.49, "Meat"),
    (72, "Baby Back Ribs Half Order", 16.99, "Meat"),
    (73, "Pork Porterhouse", 14.99, "Meat"),
    (74, "New Zealand Lamb", 22.49, "Meat"),
    (75, "Homestyle Mashed Potatoes, Aussie Fries, Baked Potato, & Sweet Potato", 2.99, "Side"),
    (76, "Fresh Seasonal Mixed Veggies, Fresh Steamed Broccoli, & Sauteed Mushrooms", 2.99, "Side"),
    (77, "Baked Potato & Chicken Tortilla Soup Cup", 4.49, "Side"),
    (78, "Steakhouse Mac & Cheese", 4.99, "Side"),
    (79, "Broccoli & Cheese", 3.99, "Side"),
    (80, "Loaded Mashed Potatoes", 3.99, "Side"),
    (81, "Grilled Asparagus", 3.99, "Side"),
    (82, "Chocolate Thunder from Down Under", 7.99, "Dessert"),
    (83, "New York-Style Cheesecake", 6.99, "Dessert"),
    (84, "Salted Caramel Topped Cheesecake", 7.99, "Dessert"),
    (85, "Triple-Layer Carrot Cake", 6.99, "Dessert"),
    (86, "Salted Caramel Cookie Skillet", 4.99, "Dessert"),
    (87, "Double Chocolate or Seasonal Parfaits", 4.99, "Dessert"),
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

con = sqlite3.connect("Chilis.db")
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS Reservations(Name TEXT, PartyCount INTEGER, Date timestamp, Time TIME, Items TEXT, Total REAL)"
)

cur.execute("CREATE TABLE IF NOT EXISTS ReservationTimes(Date timestamp, Time TIME)")
for row in reservation_times:
    cur.execute("INSERT INTO ReservationTimes VALUES (?, ?)", row)

cur.execute("CREATE TABLE IF NOT EXISTS Menu(ID INTEGER, Item TEXT, Price REAL, Type TEXT)")
for row in chilis_list:
    cur.execute("INSERT INTO Menu VALUES (?, ?, ?, ?)", row)

cur.execute(
    "CREATE TABLE IF NOT EXISTS Carryout(Name TEXT, Time TIME, Items TEXT, Total REAL)"
)

cur.execute(
    "CREATE TABLE IF NOT EXISTS Delivery(Name TEXT, Destination TEXT, DeliveryTime TIME, Items TEXT, Total REAL)"
)

cur.execute("CREATE TABLE IF NOT EXISTS Availability(Available INTEGER)")

con.commit()
con.close()


con = sqlite3.connect("Outback.db")
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS Reservations(Name TEXT, PartyCount INTEGER, Date timestamp, Time TIME, Items TEXT, Total REAL)"
)

cur.execute("CREATE TABLE IF NOT EXISTS ReservationTimes(Date timestamp, Time TIME)")
for row in reservation_times:
    cur.execute("INSERT INTO ReservationTimes VALUES (?, ?)", row)

cur.execute("CREATE TABLE IF NOT EXISTS Menu(ID INTEGER, Item TEXT, Price REAL, Type TEXT)")
for row in outbacksh_list:
    cur.execute("INSERT INTO Menu VALUES (?, ?, ?, ?)", row)

cur.execute(
    "CREATE TABLE IF NOT EXISTS Carryout(Name TEXT, Time TIME, Items TEXT, Total REAL)"
)

cur.execute(
    "CREATE TABLE IF NOT EXISTS Delivery(Name TEXT, Destination TEXT, DeliveryTime TIME, Items TEXT, Total REAL)"
)

cur.execute("CREATE TABLE IF NOT EXISTS Availability(Available INTEGER)")
con.commit()
con.close()