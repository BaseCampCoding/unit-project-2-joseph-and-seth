import random
import sqlite3
from variables import *
from datetime import date
from datetime import datetime
from datetime import timedelta


def delivery_time():
    current_time = datetime.now()
    added_time = timedelta(minutes=random.randint(30, 65))
    time = current_time + added_time
    time = time.strftime("%H:%M")
    delivery_time = f"{time}"
    print(f"\nYour estimated delivery time will be {delivery_time}\n")
    return delivery_time


def menu1():
    con = sqlite3.connect("Chilis.db")
    cur = con.cursor()
    while True:
        food_type = input(
            f"""\nWhat food category would you like to see?\n
[1] {Yellow}Appetizers{Reset}
[2] {Green}Salads{Reset}
[3] {Blue}Sandwiches{Reset}
[4] {Red}Meat{Reset}
[5] {Yellow}Mexican Food{Reset}
[6] {Green}Chicken{Reset}
[7] {Blue}Combos{Reset}
[8] {Red}Sides{Reset}
[9] {Yellow}Desserts{Reset}
[10] {Green}Kids Meals{Reset}
[11] {Blue}Beverages{Reset}
[12] {Red}Full Menu{Reset}
\n"""
        )
        if food_type.isdigit():
            food_type = int(food_type)
            break
        else:
            print("Please select a valid option!")
    if food_type == 1:
        print(f"\n{Red}Appetizers{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Appetizer'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 2:
        print(f"\n{Red}Salads{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Salad'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 3:
        print(f"\n{Red}Sandwiches{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Sandwich'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 4:
        print(f"\n{Red}Meats{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Meat'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 5:
        print(f"\n{Red}Mexican Food{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Mexican'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 6:
        print(f"\n{Red}Chicken{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Chicken'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 7:
        print(f"\n{Red}Combos{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Combo'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 8:
        print(f"\n{Red}Sides{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Sides'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 9:
        print(f"\n{Red}Desserts{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Dessert'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 10:
        print(f"\n{Red}Kid's Meals{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Kids Meals'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 11:
        print(f"\n{Red}Beverages{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Beverage'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 12:
        print(f"\n{Red}Full Menu{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    print("")


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
    while True:
        food_type = input(
            f"""\nWhat food category would you like to see?\n
[1] {Yellow}Appetizers{Reset}
[2] {Green}Soups{Reset}
[3] {Blue}Salads{Reset}
[4] {Red}Steaks{Reset}
[5] {Yellow}Seafood{Reset}
[6] {Green}Tacos{Reset}
[7] {Blue}Sandwiches{Reset}
[8] {Red}Chicken{Reset}
[9] {Yellow}Meat{Reset}
[10] {Green}Sides{Reset}
[11] {Blue}Desserts{Reset}
[12] {Red}Full Menu{Reset}
\n"""
        )
        if food_type.isdigit():
            food_type = int(food_type)
            break
        else:
            print("Please select a valid option!")
    if food_type == 1:
        print(f"\n{Red}Appetizers{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Appetizer'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 2:
        print(f"\n{Red}Soups{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Soup'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 3:
        print(f"\n{Red}Salads{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Salad'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 4:
        print(f"\n{Red}Steaks{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Steak'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 5:
        print(f"\n{Red}Seafood{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Seafood'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 6:
        print(f"\n{Red}Tacos{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Taco'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 7:
        print(f"\n{Red}Sandwiches{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Sandwich'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 8:
        print(f"\n{Red}Chicken{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Chicken'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 9:
        print(f"\n{Red}Meat{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Meat'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 10:
        print(f"\n{Red}Sides{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Side'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 11:
        print(f"\n{Red}Desserts{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu WHERE Type='Dessert'")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    elif food_type == 12:
        print(f"\n{Red}Full Menu{Reset}")
        print(
            "============================================================================"
        )
        cur.execute("SELECT * FROM Menu")
        for row in cur.fetchall():
            print(
                f"{Blue}ID{Reset}: {row[0]}, {Yellow}Item{Reset}: {row[1]}, {Green}Price{Reset}: ${row[2]}"
            )
    print("")


def menu_options2():
    con = sqlite3.connect("Outback.db")
    cur = con.cursor()
    menu2()
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
                menu2()
                break
            elif choose_more.lower() == "n" or choose_more.lower() == "no":
                break
            else:
                print("Please choose a valid option")
        if choose_more.lower() == "n" or choose_more.lower() == "no":
            break
    return total