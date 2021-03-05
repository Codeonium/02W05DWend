import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.paco = Guest("Paco", 400)
        despasito = Song("Despasito")
        no_more = Song("no_more")

        songs1 = [despasito, no_more]

        self.room1 = Room("fun", 2, songs1)

    def test_experience(self):
        pass
