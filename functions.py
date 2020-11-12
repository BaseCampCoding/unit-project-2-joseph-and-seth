import random
import json
import sqlite3
from colorama import Fore
from colorama import Style
from datetime import date
from datetime import datetime
from datetime import timedelta

dates = {}
items = []
Blue = Fore.BLUE
Red = Fore.RED
Yellow = Fore.YELLOW
Green = Fore.GREEN
Reset = Style.RESET_ALL

con = sqlite3.connect("Chilis.db")
cur = con.cursor()


def delivery_time():
    current_time = datetime.now()
    added_time = timedelta(minutes=random.randint(30, 65))
    time = current_time + added_time
    time = time.strftime("%H:%M")
    delivery_time = f"{time}"
    print(f"Your estimated delivery time will be {delivery_time}")
    return delivery_time


def menu1():
    cur.execute("SELECT * FROM Menu")
    for row in cur.fetchall():
        print(
            f"{Fore.BLUE}ID{Style.RESET_ALL}: {row[0]}, {Fore.YELLOW}Item{Style.RESET_ALL}: {row[1]}, {Fore.GREEN}Price{Style.RESET_ALL}: {row[2]}"
        )


def menu_options1():
    menu1()
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
        if choose_more.lower() == "y" or "yes":
            menu1()
        elif choose_more.lower() == "n" or "no":
            break
        else:
            print("Please choose a valid option")
    return total


con.close()

con = sqlite3.connect("Outback.db")
cur = con.cursor()


def menu2():
    cur.execute("SELECT * FROM Menu")
    for row in cur.fetchall():
        print(
            f"{Fore.BLUE}ID{Style.RESET_ALL}: {row[0]}, {Fore.YELLOW}Item{Style.RESET_ALL}: {row[1]}, {Fore.GREEN}Price{Style.RESET_ALL}: {row[2]}"
        )


def menu_options2():
    menu2()
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
        if choose_more.lower() == "y" or "yes":
            menu2()
        elif choose_more.lower() == "n" or "no":
            break
        else:
            print("Please choose a valid option")
    return total