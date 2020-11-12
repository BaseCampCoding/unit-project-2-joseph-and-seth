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


def delivery_time():
    current_time = datetime.now()
    added_time = timedelta(minutes=random.randint(30, 65))
    time = current_time + added_time
    time = time.strftime("%H:%M")
    delivery_time = f"{time}"
    print(f"Your estimated delivery time will be {delivery_time}")
    return delivery_time


def menu1():
    con = sqlite3.connect("Chilis.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Menu")
    for row in cur.fetchall():
        print(
            f"{Fore.BLUE}ID{Style.RESET_ALL}: {row[0]}, {Fore.YELLOW}Item{Style.RESET_ALL}: {row[1]}, {Fore.GREEN}Price{Style.RESET_ALL}: {row[2]}"
        )


def menu_options1():
    con = sqlite3.connect("Chilis.db")
    cur = con.cursor()
    menu1()
    total = 0
    while True:
        while True:
            id_choice = input("\nChoose the ID of the item you want to order.\n")
            if id_choice.isdigit():
                break
            else:
                print("Please choose a valid ID.")
        sqlStatement = "SELECT Price FROM Menu WHERE ID = ?"
        cur.execute(sqlStatement, [id_choice])
        for price in cur.fetchall():
            total += price[0]
        cur.execute("SELECT Item FROM Menu WHERE ID = ?", [id_choice])
        for item in cur.fetchall():
            items.append(item)
        print(f"\nYour total is currently {total:.2f}")
        while True:
            choose_more = input("\nWould you like to add any more items?\n")
            if choose_more.lower() == "y" or choose_more.lower() == "yes":
                menu1()
                break
            elif choose_more.lower() == "n" or choose_more.lower() == "no":
                break
            else:
                print("Please choose a valid option")
        if choose_more.lower() == "n" or choose_more.lower() == "no":
            break
    return total


def menu2():
    con = sqlite3.connect("Outback.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Menu")
    for row in cur.fetchall():
        print(
            f"{Fore.BLUE}ID{Style.RESET_ALL}: {row[0]}, {Fore.YELLOW}Item{Style.RESET_ALL}: {row[1]}, {Fore.GREEN}Price{Style.RESET_ALL}: {row[2]}"
        )


def menu_options2():
    con = sqlite3.connect("Outback.db")
    cur = con.cursor()
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
        if choose_more.lower() == "y" or choose_more.lower() == "yes":
            menu2()
        elif choose_more.lower() == "n" or choose_more.lower() == "no":
            break
        else:
            print("Please choose a valid option")
    return total
