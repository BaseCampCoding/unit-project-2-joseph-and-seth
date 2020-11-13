import random
import tkinter as tk
import sqlite3

top = tk.Tk()
# Code to add widgets will go here...
top.mainloop()

class Customer:
    def __init__(self):
        self.rchoice = tk.Tk()
        self.rchoice.geometry("200x100")
        self.rchoice.title("Food Line")
        button1 = tk.Button(text=" Chili's ",bg="red", height=2, width=20, command=self.select_Chilis)
        button1.grid(column=0,row=1)
        button2 = tk.Button(text=" Outback Steakhouse ",bg="Yellow", height=2, width=20, command=self.select_Outback)
        button2.grid(column=0,row=2)
        
        playAgainText = tk.Label(text="Reset?")
        playAgainText.grid(column=0, row=7)
        button6 = tk.Button(text="Yes", height=2, width=5, command=self.resetGame)
        button6.grid(column=0, row=8)
        self.rchoice.mainloop()

    # def playerDamage(self): # Shows the damage given if the player wins, with the chance of missing.
    #     playerDamage = 20
    #     global playerMiss
    #     global playerCrit
    #     missAttack = random.randint(1, 5)
    #     if missAttack == 1:
    #         playerDamage = 0
    #         print("\nYour attack missed!")
    #         playerMiss = 'Your attack missed!'
    #     critAttack = random.randint(1, 5)
    #     if playerDamage != 0 and critAttack == 1:
    #         playerDamage *= 2
    #         print("You got a critical hit!")
    #         playerCrit = 'You got a critical hit!'
    #     return playerDamage

    def resetGame(self): # Function to reset the game.
        global playerHealth
        global comHealth
        self.rchoice.destroy()
        playerHealth = 100
        comHealth = 100
        Customer()

    # def comDamage(self): # Shows the damage given if the computer wins, with the chance of missing.
    #     comDamage = 20
    #     global comMiss
    #     global comCrit
    #     missAttack = random.randint(1, 5)
    #     if missAttack == 1:
    #         comDamage = 0
    #         print("\nThe computer's attack missed!")
    #         comMiss = "The computer's attack missed!"
    #     critAttack = random.randint(1, 5)
    #     if comDamage != 0 and critAttack == 1:
    #         comDamage *= 2
    #         print("The computer got a critical hit!")
    #         comCrit = 'The computer got a critical hit!'
    #     return comDamage

    # def random_computer_choice(self): # Computer randomly chooses a type.
    #     return random.choice(choices) 

    # def result(self):
    #     cur.execute("SELECT Available FROM Availability")
    #     availability = cur.fetchone()
    #     if availability == (1,):
    #         print(f"Reservations are currently {Green}available{Reset}.")
    #     else:
    #         print(f"Reservations are currently {Red}unavailable{Reset}.")
    #     choice = int(
    #         input(
    #             f"""\nWould you like to:\n
    #     [1] Make a {Blue}reservation{Reset}
    #     [2] Order {Red}carry-out{Reset}
    #     [3] Schedule a {Yellow}delivery{Reset}
    #     """
    #         )
    #     )
    #     if choice == 1 and availability == (1,):
    #         name = input(f"\nWhat is the {Yellow}name{Reset} for this order?\n")
    #         while True:
    #             count = input(f"\nWhat is the {Red}size{Reset} of your party?\n")
    #             if count.isdigit():
    #                 count = int(count)
    #                 break
    #             else:
    #                 print("Please input a valid party size!")
    #         print(f"\nHere are our {Green}available dates{Reset}.\n")
    #         cur.execute("SELECT Date FROM ReservationTimes GROUP BY Date")
    #         for row in cur.fetchall():
    #             print(f"{Green}Date{Reset}: {row[0]}")

    #         chosen_date = input(f"\nWhich {Green}date{Reset} would you like to schedule for?\n")
    #         split_dates = chosen_date.split("/")
    #         chosen_date2 = date(int(split_dates[2]), int(split_dates[0]), int(split_dates[1]))

    #         print(f"\nHere are {Blue}available times{Reset}.\n")
    #         cur.execute("SELECT DISTINCT Date FROM ReservationTimes")
    #         for row in cur.fetchall():
    #             if chosen_date in row:
    #                 cur.execute("SELECT DISTINCT Time FROM ReservationTimes GROUP BY Time")
    #                 for row in cur.fetchall():
    #                     print(f"Time: {row[0]}")

    #         cur.execute("DELETE FROM ReservationTimes WHERE Date = ?", [chosen_date])

    #         chosen_time = input("\nWhat time would you like to schedule for?\n")
    #         if rest_choice == 1:
    #             total = menu_options1()
    #         elif rest_choice == 2:
    #             total = menu_options2()
    #         order = json.dumps(items)
    #         print(
    #             f"\nThank you for using {Yellow}Food Line{Reset}! Here is your order summary!\n"
    #         )
    #         print(f"""
    #     {Yellow}Name{Reset}: {name}, {Red}Party Count{Reset}: {count}
    #     {Green}Date{Reset}: {chosen_date2}, {Blue}Time{Reset}: {chosen_time}
    #     {Yellow}Order{Reset}: {order}
    #     {Green}Total{Reset}: ${total}
    #             """
    #         )
    #         cur.execute(
    #             "INSERT INTO Reservations VALUES (?, ?, ?, ?, ?, ?)",
    #             (name, count, chosen_date2, chosen_time, order, total),
    #         )
    #         con.commit()
    #     elif choice == 1 and availability != (1,):
    #         print("We're sorry, reservations are currently unavailable at this time.")
    #     elif choice == 2:
    #         name = input("\nWhat is the name for this order?\n")
    #         time = input("\nWhat time do you want to pick it up?\n")

    #         if rest_choice == 1:
    #             total = menu_options1()
    #         elif rest_choice == 2:
    #             total = menu_options2()
    #         order = json.dumps(items)
    #         print(
    #             f"\nThank you for using {Yellow}Food Line{Reset}! Here is your order summary!\n"
    #         )
    #         print(
    #             f"""{Yellow}Name{Reset}: {name}
    #     {Red}Time{Reset}: {time}
    #     {Blue}Order{Reset}: {order}
    #     {Green}Total{Reset}: ${total}
    #         """
    #         )

    #         cur.execute("INSERT INTO Carryout VALUES (?, ?, ?, ?)", (name, time, order, total))
    #         con.commit()
    #     elif choice == 3:
    #         name = input("What is the name for this order?\n")
    #         address = input("\nWhat is the address you want to deliver to?\n")
    #         delivery_time = delivery_time()
    #         if rest_choice == 1:
    #             total = menu_options1()
    #         elif rest_choice == 2:
    #             total = menu_options2()
    #         order = json.dumps(items)
    #         print(
    #             f"\nThank you for using {Yellow}Food Line{Reset}! Here is your order summary!\n"
    #         )
    #         print(
    #             f"""{Yellow}Name{Reset}: {name}
    #     {Red}Address{Reset}: {address}
    #     {Blue}Estimated Delivery Time{Reset}: {delivery_time}
    #     {Yellow}Order{Reset}: {order}
    #     {Green}Total{Reset}: ${total:.2f}
    #         """
    #         )
    #         cur.execute(
    #             "INSERT INTO Delivery VALUES (?, ?, ?, ?, ?)",
    #             (name, address, delivery_time, order, total),
    #         )
    #         con.commit()
    #     else:
    #         print("Please choose a valid option!")
    #         text_area = tk.Text(master=self.game,height=12,width=60,bg="#FFFF99")
    #         text_area.grid(column=0,row=6)
    #         if playerHealth <= 0:
    #             comGameWinner = 'The computer is the winner of the game!'
    #         elif comHealth <= 0:
    #             playerGameWinner = 'You are the winner of the game!'
    #         answer = '''
    #         Your Choice: {uc}
    #         Computer's Choice : {cc}
    #         Winner: {w}
    #         {pcr}{cpr}
    #         {pm}{cm}
    #         Your Health : {u}
    #         Computer Health : {c}

    #         {pgw}{cgw}
            
    #         '''.format(uc=userChoice,cc=comChoice,w=winner,pcr= playerCrit, cpr=comCrit, pm=playerMiss, cm=comMiss, u=playerHealth,c=comHealth, pgw=playerGameWinner, cgw=comGameWinner)
    #         text_area.insert(tk.END,answer)
    #         playerCrit = ''
    #         playerMiss = ''
    #         comCrit = ''
    #         comMiss = ''
    #         playerGameWinner = ''
    #         comGameWinner = ''
        

    def select_Chilis(self):
        con = sqlite3.connect('chilis.db')
        cur = con.cursor()
        text_area = tk.Text(master=self.rchoice,height=12,width=60)
        text_area.grid(column=0,row=0)
        text_area.insert(tk.END,"Chili's")

    def select_Outback(self):
        con = sqlite3.connect('chilis.db')
        cur = con.cursor()
        text_area = tk.Text(master=self.rchoice,height=12,width=60)
        text_area.grid(column=0,row=0)
        text_area.insert(tk.END,"Outback Steakhouse")

    # def availability_message():
    #     cur.execute("SELECT Available FROM Availability")
    #     availability = cur.fetchone()
    #     if availability == (1,):
    #         print(f"Reservations are currently {Green}available{Reset}.")
    #     else:
    #         print(f"Reservations are currently {Red}unavailable{Reset}.")

    # def ice(self):
    #     global userChoice
    #     global comChoice
    #     userChoice='Ice'
    #     comChoice=self.random_computer_choice() 
    #     self.result(userChoice,comChoice)

    # def rock(self):
    #     global userChoice
    #     global comChoice
    #     userChoice= 'Rock'
    #     comChoice=self.random_computer_choice() 
    #     self.result(userChoice,comChoice)

    # def ground(self):
    #     global userChoice
    #     global comChoice
    #     userChoice='Ground'
    #     comChoice=self.random_computer_choice() 
    #     self.result(userChoice,comChoice) 


# Customer()