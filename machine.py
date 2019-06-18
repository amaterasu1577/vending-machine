from enum import Enum

class Slot:
    """ Class Slot """
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = 0

class Coin(Enum):
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    DOLLAR = 100

Coin.NICKEL # => 5

class Machine:
    def __init__(self, slot_list):
        self.slots = { slot.code: slot for slot in slot_list }
        self.amount = 0
        # TODO: self.coins (dict)

    def refill(self, code, count):
        self.slots[code].quantity += count

    def insert_coin(self, value):
         self.amount += value

    def press(self, code):
        slot = self.slots[code]
        if self.amount >= slot.price:
            slot.quantity -= 1
            self.amount -= slot.price


