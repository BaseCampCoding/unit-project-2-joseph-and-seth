import random
import json
import sqlite3
from colorama import Fore
from colorama import Style
from datetime import date
from datetime import datetime

dates = {}
items = []

con = sqlite3.connect("restaraunt_1.db")
cur = con.cursor()


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