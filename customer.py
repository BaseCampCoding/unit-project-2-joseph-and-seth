from functions import *

Blue = Fore.BLUE
Red = Fore.RED
Yellow = Fore.YELLOW
Green = Fore.GREEN
Reset = Style.RESET_ALL

con = sqlite3.connect("restaraunt_1.db")
cur = con.cursor()

print(f"Welcome to {Yellow}Food Line{Reset}! Home to all your restaraunt needs!")

cur.execute("SELECT Available FROM Availability")
availability = cur.fetchone()
if availability == (1,):
    print(f"Reservations are currently {Green}available{Reset}.")
else:
    print(f"Reservations are currently {Red}unavailable{Reset}.")
choice = input(
    f"""Would you like to:
[1] Make a {Blue}reservation{Reset}
[2] Order {Red}carry-out{Reset}
[3] Schedule a {Yellow}delivery{Reset}
"""
)
if choice == "1" and availability == (1,):
    name = input(f"\nWhat is the {Yellow}name{Reset} for this order?\n")
    count = input(f"\nWhat is the {Red}size{Reset} of your party?\n")
    print(f"\nHere are our {Green}available dates{Reset}.\n")
    cur.execute("SELECT Date FROM ReservationTimes")
    for row in cur.fetchall():
        print(f"{Green}Date{Reset}: {row[0]}")

    chosen_date = input(f"\nWhat {Green}date{Reset} would you like to schedule for?\n")
    split_dates = chosen_date.split("/")
    chosen_date2 = date(int(split_dates[2]), int(split_dates[0]), int(split_dates[1]))

    print(f"\nHere are {Blue}available times{Reset}.\n")
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

    cur.execute("INSERT INTO Carryout VALUES (?, ?, ?, ?)", (name, time, order, total))
    con.commit()
elif choice == "3":
    name = input("What is the name for this order?\n")
    address = input("What is the address you want to deliver to?\n")
    delivery_time = delivery_time()
    total = menu_options()
    order = json.dumps(items)

    cur.execute(
        "INSERT INTO Delivery VALUES (?, ?, ?, ?, ?)",
        (name, address, delivery_time, order, total),
    )
    con.commit()