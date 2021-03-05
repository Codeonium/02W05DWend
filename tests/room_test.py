import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("80's", 1, [],25 )
        self.room2 = Room("90's", 2, [],20 )
        self.room3 = Room("00's", 3, [],10 )
        self.room4 = Room("70's", 4, [],15 )
        self.room5 = Room("60's", 5, [],5 )
        self.room6 = Room("Music from before time was invented", 6, [],50 )
        self.waiting_room = Room("Elevate your scamp", 7, "Best of Elevator Music",200 )
    
    def test_room_has_name_1(self):
        self.assertEqual("80's", self.room1.name)

    def test_room_has_name_2(self):
        self.assertEqual("90's", self.room2.name)

    def test_room_has_name_3(self):
        self.assertEqual("00's", self.room3.name)

    def test_room_has_name_4(self):
        self.assertEqual("70's", self.room4.name)

    def test_room_has_name_5(self):
        self.assertEqual("60's", self.room5.name)

    def test_room_has_name_6(self):
        self.assertEqual("Music from before time was invented", self.room6.name)

    def test_room_has_name_7(self):
        self.assertEqual("Elevate your scamp", self.waiting_room.name)
    
