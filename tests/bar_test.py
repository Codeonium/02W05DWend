import unittest

from classes.bar import Bar

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.beer = Bar("Beer", 2, 1, 1)
        self.proseco = Bar("Proseco", 10, 3, 4)
        self.vodka = Bar("Vodka", 5, 2, 5)