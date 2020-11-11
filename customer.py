from datetime import date
from datetime import datetime
import random
import sqlite3
from colorama import Style
from colorama import Fore
import json

time_choices = ["4:00", "4:30", "5:00", "5:30", "6:00", "6:30", "7:00", "7:30", "8:00"]
dates = {}
items = []

con = sqlite3.connect("restaraunt_1.db")
cur = con.cursor()


def choose_times():
    random_times = random.choices(time_choices)
    return random_times


def menu():
    cur.execute("SELECT * FROM Menu")
    for row in cur.fetchall():
        print(
            f"{Fore.BLUE}ID{Style.RESET_ALL}: {row[0]}, {Fore.YELLOW}Item{Style.RESET_ALL}: {row[1]}, {Fore.GREEN}Price{Style.RESET_ALL}: {row[2]}"
        )


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


def delivery_time():
    current_time = get_time()
    time = random.randint(30, 120)
    delivery_time = f"{(int(current_time[1]) + (time // 60))}:{(int(current_time[3]) + (time % 60))}"
    print(f"Your estimated delivery time will be {delivery_time}")
    return delivery_time


def menu_options():
    menu()
    total = 0
    while True:
        id_choice = input("\nChoose the ID of the item you want to order.\n")
        sqlStatement = "SELECT Price FROM Menu WHERE ID = ?"
        cur.execute(sqlStatement, [id_choice])
        for price in cur.fetchall():
            total += price[0]
        cur.execute("SELECT Item FROM Menu WHERE ID = ?", [id_choice])
        for item in cur.fetchall():
            items.append(item)
        print(f"\nYour total is currently {total:.2f}")
        choose_more = input("\nWould you like to add any more items?\n")
        if choose_more.lower() == "y":
            menu()
        elif choose_more.lower() == "n":
            break
        else:
            print("Please choose a valid option")
    return total


print(
    f"Welcome to {Fore.YELLOW}Food Line{Style.RESET_ALL}! Home to all your restaraunt needs!"
)
cur.execute("SELECT Available FROM Availability")
availability = cur.fetchone()
if availability == (1,):
    print(f"Reservations are currently {Fore.GREEN}available{Style.RESET_ALL}.")
else:
    print(f"Reservations are currently {Fore.RED}unavailable{Style.RESET_ALL}.")
choice = input(
    f"""Would you like to:
[1] Make a {Fore.BLUE}reservation{Style.RESET_ALL}
[2] Order {Fore.RED}carry-out{Style.RESET_ALL}
[3] Schedule a {Fore.YELLOW}delivery{Style.RESET_ALL}
"""
)
if choice == "1" and availability == (1,):
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
    total = menu_options()
    order = json.dumps(items)
    cur.execute(
        "INSERT INTO Reservations VALUES (?, ?, ?, ?, ?, ?)",
        (name, count, chosen_date2, chosen_time, order, total),
    )
    con.commit()
elif choice == "1" and availability != (1,):
    print("We're sorry, reservations are currently unavailable at this time.")
elif choice == "2":
    name = input("\nWhat is the name for this order?\n")
    time = input("\nWhat time do you want to pick it up?\n")

    total = menu_options()
    order = json.dumps(items)

    cur.execute("INSERT INTO Carryout VALUES (?, ?, ?)", (name, time, order, total))
    con.commit()
elif choice == "3":
    name = input("What is the name for this order?")
    address = input("What is the address you want to deliver to?")
    delivery_time = delivery_time()
    total = menu_options()
    order = json.dumps(items)

    cur.execute(
        "INSERT INTO Delivery VALUES (?, ?, ?, ?)",
        (name, address, delivery_time, order, total),
    )
    con.commit()