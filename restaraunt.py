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

if action == "View":
    cur.execute('SELECT * FROM Reservations')
    for row in cur.fetchall():
        print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}")
        print('')
elif action == "Menu":
    cur.execute('SELECT * FROM Menu')
    for row in cur.fetchall():
        print(f"{row[0]}, {row[1]}")
        print('')
elif action.lower() == "availability":
    cur.execute('SELECT Available FROM Availability')
    availability = cur.fetchone()
    if availability == True:
        print("Reservations are currently available")
    else:
        print("Reservations are currently unavailable.")
    changed_availability = input("What would you like to set the availability to?")
    if changed_availability.lower() == "available":
        cur.execute('INSERT INTO Availability VALUES(1)')
    elif changed_availability.lower() == "unavailable":
        cur.execute('INSERT INTO Availability VALUES(0)')
    else:
        print("Please choose a valid option")
else:
    print("HI")
    



# def input_party_size(prompt: str) -> int:
#     while True:
#         response = input(prompt)
#         if response.isdigit():
#             response = int(response)
#             if response >= 0:
#                 return response
#         print('Select a value of 1 or greater for the party size.')