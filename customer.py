from functions import *

con = sqlite3.connect("restaraunt_1.db")
cur = con.cursor()

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