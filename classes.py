from variables import *

class Reservation():
    def __init__(self, name, party_count, date, time, order, total):
        self.name = name
        self.party_count = party_count
        self.date = date
        self.time = time
        self.order = order
        self.total = total
        
    def __str__(self):
        return f"""
{Yellow}Name{Reset}: {self.name}, {Red}Party Count{Reset}: {self.party_count}
{Green}Date{Reset}: {self.date}, {Blue}Time{Reset}: {self.time}
{Yellow}Order{Reset}: {self.order}
{Green}Total{Reset}: ${self.total}
        """

class Carryout():
    def __init__(self, name, time, order, total):
        self.name = name
        self.time = time
        self.order = order
        self.total = total
        
    def __str__(self):
        return f"""
{Yellow}Name{Reset}: {self.name}
{Blue}Time{Reset}: {self.time}
{Yellow}Order{Reset}: {self.order}
{Green}Total{Reset}: ${self.total}
"""

class Delivery():
    def __init__(self, name, address, delivery_time, order, total):
        self.name = name
        self.address = address
        self.delivery_time = delivery_time
        self.order = order
        self.total = total
        
    def __str__(self):
        return f"""
{Yellow}Name{Reset}: {self.name}, 
{Red}Address{Reset}: {self.address}
{Blue}Estimated Delivery Time{Reset}: {self.delivery_time}
{Yellow}Order{Reset}: {self.order}
{Green}Total{Reset}: ${self.total}
"""