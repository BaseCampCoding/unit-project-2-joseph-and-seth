from datetime import date
import random
import sqlite3
from colorama import Style
from colorama import Fore

time_choices = ["4:00", "4:30", "5:00", "5:30", "6:00", "6:30", "7:00", "7:30", "8:00"]
dates = {}

con = sqlite3.connect("restaraunt_1.db")
cur = con.cursor()


def choose_times():
    random_times = random.choices(time_choices)
    return random_times


def menu():
    cur.execute("SELECT * FROM Menu")
    for row in cur.fetchall():
        print(f"ID: {row[0]}, Item: {row[1]}, Price: {row[2]}")


print(
    f"Welcome to {Fore.YELLOW}Food Line{Style.RESET_ALL}! Home to all your restaraunt needs!"
)
cur.execute("SELECT Available FROM Availability")
availability = cur.fetchone()
if availability == (1,):
    print("Reservations are currently available")
else:
    print("Reservations are currently unavailable.")
choice = input(
    f"""Would you like to:
- Make a [{Fore.BLUE}reservation{Style.RESET_ALL}]
- Order [{Fore.RED}carry-out{Style.RESET_ALL}]
- Schedule a [{Fore.YELLOW}delivery{Style.RESET_ALL}]
"""
)
if choice == "reservation" and availability == (1,):
    name = input("\nWhat is the name for this order?\n")
    count = input("\nWhat is the size of your party?\n")
    print("\nHere are our available dates.\n")
    cur.execute("SELECT Date FROM ReservationTimes")
    for row in cur.fetchall():
        print(f"Date: {row[0]}")

    chosen_date = input("\nWhat date would you like to schedule for?\n")
    split_dates = chosen_date.split("/")
    chosen_date2 = date(int(split_dates[2]), int(split_dates[0]), int(split_dates[1]))

    print("\nHere are available times.\n")
    cur.execute("SELECT Date FROM ReservationTimes")
    for row in cur.fetchall():
        if chosen_date in row:
            cur.execute("SELECT Time FROM ReservationTimes")
            for row in cur.fetchall():
                print(f"Time: {row[0]}")

    cur.execute("DELETE FROM ReservationTimes WHERE Date = ?", [chosen_date])

    chosen_time = input("\nWhat time would you like to schedule for?\n")
    menu()
    total = 0
    while True:
        id_choice = input("\nChoose the ID of the item you want to order.\n")
        sqlStatement = "SELECT Price FROM Menu WHERE ID = ?"
        cur.execute(sqlStatement, [id_choice])
        for price in cur.fetchall():
            total += price[0]
        print(f"\nYour total is currently {total:.2f}")
        choose_more = input("\nWould you like to add any more items?\n")
        if choose_more.lower() == "y":
            menu()
        elif choose_more.lower() == "n":
            break
        else:
            print("Please choose a valid option")
    cur.execute(
        "INSERT INTO Reservations VALUES (?, ?, ?, ?, ?)",
        (name, count, chosen_date2, chosen_time, total),
    )
    con.commit()
elif choice == "reservation" and availability != (1,):
    print("We're sorry, reservations are currently unavailable at this time.")