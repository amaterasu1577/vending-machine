"""
Implement a vending machine
"""
from enum import Enum


class Slot():
    """ Class Slot to implement a slot in vending machine """
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = 0

class Coin(Enum):
    """ Enumeration of coins values """
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    DOLLAR = 100

class Machine:
    """ Implement a vending machine """
    # Default number of slots in a machine
    NB_SLOT = 4
    def __init__(self, slot_list):
        self.slots = {slot.code: slot for slot in slot_list}
        self.amount = 0
        self.coins = {}

    def refill(self, code, count):
        """ Refill the machine with slots """
        self.slots[code].quantity += count

    def refill_coins(self, coins_list):
        """ Refill the machine with slots """
        self.coins = coins_list

    def insert_coin(self, value):
        """ Insertion of coin action """
        self.amount += value

    def press(self, code):
        """ Render the client choice """
        slot = self.slots[code]
        if self.amount >= slot.price:
            slot.quantity -= 1
            self.amount -= slot.price
