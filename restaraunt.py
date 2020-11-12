import sqlite3
from functions import menu1
from functions import menu2
from variables import *


# Asks the user which restaurant they work at.
rc = int(
    input(
        f"""Select which {Blue}restaurant{Reset} you work at:
[1] {Red}Chili's{Reset}
[2] {Yellow}Outback Steakhouse{Reset}
"""
    )
)

if rc == 1:
    con = sqlite3.connect("Chilis.db")
    cur = con.cursor()
elif rc == 2:
    con = sqlite3.connect("Outback.db")
    cur = con.cursor()


# Presents user with menu options of what they can do.
while True:
    print(f"{Yellow}Food Line{Reset} Staff Menu")
    action = int(
        input(
            f"""Would you like to:
[1] View queued {Yellow}orders
[2] Change {Blue}menu{Reset} select
[3] Check {Green}availability{Reset} for a guest/guests on the waiting list select
[4] {Red}Quit{Reset}
"""
        )
    )

    # Views the reservations, carry-out orders, and delivery orders in the queue list.
    if action == 1:
        while True:
            view_options = int(
                input(
                    f"""What would you like to view? 
[1] View {Blue}Reservations{Reset}
[2] View {Red}Carry-out{Reset} orders
[3] View {Yellow}Delivery{Reset} orders
[4] Return to the {Green}main menu{Reset}
"""
                )
            )
            if view_options == 1:
                cur.execute("SELECT * FROM Reservations")
                for row in cur.fetchall():
                    print(
                        f"""{Yellow}Name{Reset}: {row[0]}, {Red}Party Count{Reset}: {row[1]}
{Green}Date{Reset}: {row[2]}, {Blue}Time{Reset}: {row[3]}
{Yellow}Order{Reset}: {row[4]}
{Green}Total{Reset}: ${row[5]}
\n\n"""
                    )
            elif view_options == 2:
                cur.execute("SELECT * FROM Carryout")
                for row in cur.fetchall():
                    print(
                        f"""{Yellow}Name{Reset}: {row[0]}
{Red}Pickup Time{Reset}: {row[1]}
{Blue}Order{Reset}: {row[2]}
{Green}Total{Reset}: ${row[3]}
\n\n"""
                    )
            elif view_options == 3:
                cur.execute("SELECT * FROM Delivery")
                for row in cur.fetchall():
                    print(
                        f"""Name: {row[0]}
Destination: {row[1]}
Estimated Delivery Time: {row[2]}
Order: {row[3]}
Total: ${row[4]}
"""
                    )
            elif view_options == 4:
                print("Returning to the main menu.")
                break

    # If the user chooses menu they should have options of what they might want to do the menu.
    elif action == 2:
        while True:
            choice = int(
                input(
                    """What option would you like to select?:
- View the current menu [1]
- Change the current menu [2]
- Add to the current menu [3]
- Delete from the current menu [4]
- Return to the main menu [5]
"""
                )
            )
            # Should allow the user be able to see the current menu or changes to the menu.
            if choice == 1 and rc == 1:
                menu1()
            elif choice == 1 and rc == 2:
                menu2()
                # Should allow the user to change the menu.
            if choice == 2:
                id_number = input("What is the ID of the item you are changing? ")
                change_option = input("What value would you like to change? ")
                # The user can change the item
                if change_option.lower() == "item":
                    new_name = input(
                        "What would you like to change this item's name to? "
                    )
                    cur.execute(
                        "UPDATE Menu SET Item = ? WHERE ID = ?",
                        [new_name, id_number],
                    )
                    con.commit()
                # The user can change the price
                elif change_option.lower() == "price":
                    new_price = input(
                        "What would you like to change this item's price to? "
                    )
                    cur.execute(
                        "UPDATE Menu SET Price = ? WHERE ID = ?",
                        [new_price, id_number],
                    )
                    con.commit()
                # The user can add a new item, name of the item, and price of the item.
            elif choice == 3:
                item_id = input("What will be the ID of the new item? ")
                item_name = input("What will be the name of the new item? ")
                item_price = input("What will be the new price of the item? ")
                cur.execute(
                    "INSERT INTO Menu VALUES (?, ?, ?)",
                    (item_id, item_name, item_price),
                )
                con.commit()
            # The user can delete an item.
            elif choice == 4:
                del_item_id = input("What is the ID you want to delete? ")
                cur.execute("DELETE FROM Menu WHERE ID = ?", [del_item_id])
                con.commit()
            # The user can quit to the main menu.
            elif choice == 5:
                print("Returning to the main menu.")
                break

    # The user can see the times available for a reservation.
    elif action == 3:
        # The user can change what times and dates are available and are removed from the list or added back.
        availability_choice = int(
            input(
                """What would you like to change about availability?
[1] Set Availability
[2] Provide new available times
[3] Return to the main menu
"""
            )
        )
        if availability_choice == 1:
            cur.execute("SELECT Available FROM Availability")
            availability = cur.fetchone()
            if availability == (1,):
                print("Reservations are currently available")
            else:
                print("Reservations are currently unavailable.")
            changed_availability = input(
                "What would you like to set the availability to? "
            )
            if changed_availability.lower() == "available":
                cur.execute("DELETE FROM Availability")
                cur.execute("INSERT INTO Availability VALUES(1)")
                con.commit()
            elif changed_availability.lower() == "unavailable":
                cur.execute("DELETE FROM Availability")
                cur.execute("INSERT INTO Availability VALUES(0)")
                con.commit()
            else:
                print("Please choose a valid option.")
        elif availability_choice == 2:
            print("Here are the currently available reservation times.")
            cur.execute("SELECT * FROM ReservationTimes")
            for row in cur.fetchall():
                print(f"Date: {row[0]}, Time: {row[1]}")
            date = input("What date would you like to add to the reservation list? ")
            time = input("What times would you like to add to the reservation list? ")
            cur.execute("INSERT INTO ReservationTimes VALUES (?, ?)", (date, time))
            con.commit()
        elif availability_choice == 3:
            print("Returning to the main menu.")

    # Exits the application.
    elif action == 4:
        print("Exiting Application.")
        break