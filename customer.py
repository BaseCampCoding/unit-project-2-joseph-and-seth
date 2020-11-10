from datetime import date
import random
import sqlite3

time_choices = ["4:00", "4:30", "5:00", "5:30", "6:00", "6:30", "7:00", "7:30", "8:00"]
dates = {}

con = sqlite3.connect("restaraunt_1.db")
cur = con.cursor()


def random_date():
    start_dt = date.today().toordinal()
    end_dt = date(2020, 12, 31).toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day


def random_dates():
    global dates
    for i in range(10):
        dates["Date %s" % i] = random_date()
    for key in dates:
        print(f"{dates[key]}")


def choose_times():
    random_times = random.choices(time_choices)
    return random_times


def menu():
    cur.execute("SELECT * FROM Menu")
    for row in cur.fetchall():
        print(f"ID: {row[0]}, Item: {row[1]}, Price: {row[2]}")


print("Welcome to Food Line! Home to all your restaraunt needs!")
choice = input(
    """Would you like to:
- Make a [reservation]
- Order [carry-out]
- Schedule a [delivery]
"""
)
if choice == "reservation":
    name = input("\nWhat is the name for this order?\n")
    count = input("\nWhat is the size of your party?\n")
    print("\nHere are our available dates.\n")

    random_dates()

    chosen_date = input("\nWhat date would you like to schedule for?\n")
    split_dates = chosen_date.split("-")
    chosen_date = date(int(split_dates[0]), int(split_dates[1]), int(split_dates[2]))

    print("\nHere are available times.\n")
    if chosen_date in dates.values():
        times = {}
        for i in range(6):
            times["Time %s" % i] = choose_times()
        for key in times:
            print(f"{times[key]}")

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
        (name, count, chosen_date, chosen_time, total),
    )
    con.commit()