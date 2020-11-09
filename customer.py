print("Welcome to Food Line! Home to all your restaraunt needs!")
choice = input('''Would you like to:
- Make a [reservation]
- Order [carry-out]
- Schedule a [delivery]
''')
if choice == "reservation":
    name = input("What is the name for this order?\n")
    count = input("What is the size of your party?\n")
    print('''Here are our available dates and times.
    ''')