import sqlite3



con = sqlite3.connect('restaraunt_1.db')
cur = con.cursor()



print("Food Line Staff Menu")
action = input('''Would you like to:
- View queued reservations select [View]
- Change menu select [Menu]
- Check availability for a guest/guests on the waiting list select [Availability]
- Quit the menu select [Quit]
''')

if action.lower() == "view":
    cur.execute('SELECT * FROM Reservations')
    for row in cur.fetchall():
        print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}")
        print('')
elif action.lower() == "menu":
    choice = input("What option would you like to select?")
    if choice.lower() == "view":
        cur.execute('SELECT * FROM Menu')
        print(cur.fetchall())
    #change 
    elif action.lower() == "add":
        item_id = input('What will be the ID of the new item?')
        item_name = input('What will be the name of the new item?')
        item_price = input('What will be the new price of the item?')
        cur.execute('INSERT INTO Menu VALUES (?, ?, ?)', (item_id, item_name, item_price))

    #delete
elif action.lower() == "availability":
    cur.execute('SELECT Available FROM Availability')
    availability = cur.fetchone()
    if availability == (1,):
        print("Reservations are currently available")
    else:
        print("Reservations are currently unavailable.")
    changed_availability = input("What would you like to set the availability to?")
    if changed_availability.lower() == "available":
        cur.execute('DELETE FROM Availability')
        cur.execute('INSERT INTO Availability VALUES(1)')
        con.commit()
    elif changed_availability.lower() == "unavailable":
        cur.execute('DELETE FROM Availability')
        cur.execute('INSERT INTO Availability VALUES(0)')
        con.commit()
    else:
       print("Please choose a valid option")
elif action.lower() == "quit":
    print("Shutting down.")       
    

