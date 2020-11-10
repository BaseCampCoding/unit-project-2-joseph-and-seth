import sqlite3



con = sqlite3.connect('restaraunt_1.db')
cur = con.cursor()


# Presents user with menu options of what they can do.
print("Food Line Staff Menu")
action = input('''Would you like to:
- View queued reservations select [View]
- Change menu select [Menu]
- Check availability for a guest/guests on the waiting list select [Availability]
- Shutdowns the device [Shutdown]
''')


# Views the reservations in the queue.
if action.lower() == "view":
    cur.execute('SELECT * FROM Reservations')
    for row in cur.fetchall():
        print(f"Name: {row[0]}, Party Count: {row[1]}, Date: {row[2]}, Time: {row[3]}, Total: {row[4]}\n")
# If the user chooses menu they should have options of what they might want to do the the menu.
elif action.lower() == "menu":
    choice = input("""What option would you like to select?:
- View the current menu [View]
- Change the current menu [Change]
- Add to the current menu [Add]
- Delete from the current menu [Delete]
- Quit the menu select [Quit]
""")
# Should allow the user be able to see the current menu or changes to the menu.
    if choice.lower() == "view":
        cur.execute('SELECT * FROM Menu')
        for row in cur.fetchall():
            print(f"ID: {row[0]}, Item: {row[1]}, Price: {row[2]}")
# Should allow the user to change the menu.
    elif choice.lower() == "change":
        id_number = input("What is the ID of the item you are changing? ")
        change_option = input("What value would you like to change? ")
# The user can change the item
        if change_option.lower() == "item":
            new_name = input("What would you like to change this item's name to? ")
            cur.execute('UPDATE Menu SET Item = ? WHERE ID = ?', [new_name, id_number])
            con.commit()
# The user can change the price
        elif change_option.lower() == "price":
            new_price = input("What would you like to change this item's price to? ")
            cur.execute('UPDATE Menu SET Price = ? WHERE ID = ?', [new_price, id_number])
            con.commit()
# The user can add a new item, name of the item, and price of the item.
    elif choice.lower() == "add":
        item_id = input('What will be the ID of the new item? ')
        item_name = input('What will be the name of the new item? ')
        item_price = input('What will be the new price of the item? ')
        cur.execute('INSERT INTO Menu VALUES (?, ?, ?)', (item_id, item_name, item_price))
        con.commit()
# The user can delete an item.
    elif choice.lower() == "delete":
        del_item_id = input('What is the ID you want to delete? ')
        cur.execute('DELETE FROM Menu WHERE ID = ?', [del_item_id])
        con.commit()
# The user can quit to the main menu.
    elif choice.lower() == "quit":
        print("Heading back to the home menu")


# The user can see the times available for a reservation.
elif action.lower() == "availability":
# The user can change what times and dates are available and are removed from the list or added back.
    availability_choice = int(input("""What would you like to change about availability?
[1] Set Availability
[2] Provide new available times.
"""))
    if availability_choice == 1:
        cur.execute('SELECT Available FROM Availability')
        availability = cur.fetchone()
        if availability == (1,):
            print("Reservations are currently available")
        else:
            print("Reservations are currently unavailable.")
        changed_availability = input("What would you like to set the availability to? ")
        if changed_availability.lower() == "available":
            cur.execute('DELETE FROM Availability')
            cur.execute('INSERT INTO Availability VALUES(1)')
            con.commit()
        elif changed_availability.lower() == "unavailable":
            cur.execute('DELETE FROM Availability')
            cur.execute('INSERT INTO Availability VALUES(0)')
            con.commit()
        else:
            print("Please choose a valid option.")
    elif availability_choice == 2:     
        cur.execute('SELECT * FROM ReservationTimes')
        for row in cur.fetchall():
            print(f"Date: {row[0]}, Time: {row[1]}")
# Turns off the device. 
elif action.lower() == "Shutdown":
    print("Shutting down.")       
    

