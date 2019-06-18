# tests/test_machine.py
import unittest
from machine import Slot, Machine

class MachineTest(unittest.TestCase):
    def test_can_refill_biscuits(self):
        slots = [ Slot("A", "Chocolate Biscuits", 100) ]
        machine = Machine(slots)
        machine.refill("A", 3)

        self.assertEqual(machine.slots["A"].quantity, 3)

    def test_can_refill_coins(self):
        slots = [ Slot("A", "Chocolate Biscuits", 100) ]
        machine = Machine(slots)
        coins = {'NICKEL': 10, 'DIME': 10, 'QUARTER': 10, 'DOLLAR': 5 }
        machine.refill_coins(coins)

        self.assertEqual(machine.coins['QUARTER'], 10)

    def test_user_can_buy_item_b(self):
        slots = [ Slot("B", "Coca", 120) ]
        machine = Machine(slots)

        machine.refill("B", 1)

        machine.insert_coin(100)
        machine.insert_coin(25)
        machine.press("B")

        self.assertEqual(machine.slots["B"].quantity, 0)
        self.assertEqual(machine.amount, 5)

    def test_user_cant_buy_item_b_if_not_enough_money_inserted(self):
        slots = [ Slot("B", "Coca", 120) ]
        machine = Machine(slots)

        machine.refill("B", 5)
        machine.insert_coin(100)
        machine.insert_coin(10)
        machine.press("B")

        self.assertEqual(machine.slots["B"].quantity, 5)
        self.assertEqual(machine.amount, 110)





