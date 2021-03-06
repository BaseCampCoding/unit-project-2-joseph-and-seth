from functions import *
from classes import *
import json
import pickle

print(f"\nWelcome to {Yellow}Food Line{Reset}! Home to all your restaraunt needs!\n")
rest_choice = int(
    input(
        f"""Which restaurant would you like to place an order at?
[1] {Red}Chili's{Reset}
[2] {Yellow}Outback Steakhouse{Reset}\n"""
    )
)
if rest_choice == 1:
    con = sqlite3.connect("Chilis.db")
    cur = con.cursor()
elif rest_choice == 2:
    con = sqlite3.connect("Outback.db")
    cur = con.cursor()
cur.execute("SELECT Available FROM Availability")
availability = cur.fetchone()
if availability == (1,):
    print(f"Reservations are currently {Green}available{Reset}.")
else:
    print(f"Reservations are currently {Red}unavailable{Reset}.")
choice = int(
    input(
        f"""\nWould you like to:\n
[1] Make a {Blue}reservation{Reset}
[2] Order {Red}carry-out{Reset}
[3] Schedule a {Yellow}delivery{Reset}
"""
    )
)
if choice == 1 and availability == (1,):
    name = input(f"\nWhat is the {Yellow}name{Reset} for this order?\n")
    while True:
        count = input(f"\nWhat is the {Red}size{Reset} of your party?\n")
        if count.isdigit():
            count = int(count)
            break
        else:
            print("Please input a valid party size!")
    print(f"\nHere are our {Green}available dates{Reset}.\n")
    cur.execute("SELECT Date FROM ReservationTimes GROUP BY Date")
    for row in cur.fetchall():
        print(f"{Green}Date{Reset}: {row[0]}")

    chosen_date = input(f"\nWhich {Green}date{Reset} would you like to schedule for?\n")
    split_dates = chosen_date.split("/")
    chosen_date2 = date(int(split_dates[2]), int(split_dates[0]), int(split_dates[1]))

    print(f"\nHere are {Blue}available times{Reset}.\n")
    cur.execute("SELECT DISTINCT Date FROM ReservationTimes")
    for row in cur.fetchall():
        if chosen_date in row:
            cur.execute("SELECT DISTINCT Time FROM ReservationTimes GROUP BY Time")
            for row in cur.fetchall():
                print(f"Time: {row[0]}")

    cur.execute("DELETE FROM ReservationTimes WHERE Date = ?", [chosen_date])

    chosen_time = input(f"\nWhat {Blue}time{Reset} would you like to schedule for?\n")
    if rest_choice == 1:
        total = menu_options1()
    elif rest_choice == 2:
        total = menu_options2()
    order = json.dumps(items)
    reservation = Reservation(name, count, chosen_date2, chosen_time, order, total)
    print(
        f"\nThank you for using {Yellow}Food Line{Reset}! Here is your order summary!"
    )
    print(reservation)

    cur.execute(
        "INSERT INTO Reservations VALUES (?, ?, ?, ?, ?, ?)",
        (name, count, chosen_date2, chosen_time, order, total),
    )
    con.commit()
elif choice == 1 and availability != (1,):
    print("We're sorry, reservations are currently unavailable at this time.")
elif choice == 2:
    name = input("\nWhat is the name for this order?\n")
    time = input("\nWhat time do you want to pick it up?\n")

    if rest_choice == 1:
        total = menu_options1()
    elif rest_choice == 2:
        total = menu_options2()
    order = json.dumps(items)
    carryout = Carryout(name, time, order, total)
    print(
        f"\nThank you for using {Yellow}Food Line{Reset}! Here is your order summary!"
    )
    print(carryout)

    cur.execute("INSERT INTO Carryout VALUES (?, ?, ?, ?)", (name, time, order, total))
    con.commit()
elif choice == 3:
    name = input("What is the name for this order?\n")
    address = input("\nWhat is the address you want to deliver to?\n")
    delivery_time = delivery_time()
    if rest_choice == 1:
        total = menu_options1()
    elif rest_choice == 2:
        total = menu_options2()
    order = json.dumps(items)
    delivery = Delivery(name, address, delivery_time, order, total)
    print(
        f"\nThank you for using {Yellow}Food Line{Reset}! Here is your order summary!"
    )
    print(delivery)
    cur.execute(
        "INSERT INTO Delivery VALUES (?, ?, ?, ?, ?)",
        (name, address, delivery_time, order, total),
    )
    con.commit()
else:
    print("Please choose a valid option!")