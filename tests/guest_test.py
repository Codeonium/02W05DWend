import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("myself", 200)

    def test_guest_can_pay(self):
        self.guest.pay_entry_fee(20)
        self.assertEqual(180, self.guest.money)