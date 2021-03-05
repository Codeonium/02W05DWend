import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("myself", 200)

    def test_guest_can_pay(self):
        self.guest.pay(30)
        self.assertEqual(170, self.guest.money)