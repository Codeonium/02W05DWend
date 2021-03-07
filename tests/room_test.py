import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("80's", 1, [], [],25, [])
        self.room2 = Room("90's", 2, [], [],20, [])
        self.room3 = Room("00's", 3, [], [],10, [])
        self.room4 = Room("70's", 4, [], [],15, [])
        self.room5 = Room("60's", 5, [], [],5, [])
        self.room6 = Room("Music from before time was invented", 6, [], [], 50, [])
        self.waiting_room = Room("Elevate your scamp", 7, "Best of Elevator Music", [], 200, [])
        self.new_song = Song("Take On Me", "80's", 1.50, 244)
        self.new_song1 = Song("Bohemia Rapsody", "80's", 2.00, 354)
        self.bert = Guest ("Bert", 200, "Bohemia Rapsody" )
        self.tom = Guest ("Tom", 100, "Rocket Man")
        self.william = Guest ("William", 50, "Twist")


    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.room1, self.tom)
        self.room1.add_guest_to_room(self.room1, self.bert)
        self.assertEqual(2, self.room1.number_of_guests_in_room(self.room1))

    def test_reduce_space_from_room(self):
        self.room1.add_guest_to_room(self.room1, self.tom)
        self.room1.add_guest_to_room(self.room1, self.bert)
        self.assertEqual(23, self.room1.reduce_space_from_room(self.room1))


    def test_increase_space_in_room(self):
        pass
    
    def test_profit_from_room(self):
        pass
    
    def test_total_profit(self):
        pass
    
    def test_room_limit(self):
        pass

    def test_find_guest_by_name(self):
        pass

    def test_entry_denied(self):
        pass

    def test_entry_approved(self):
        pass

    def test_move_from_waiting_room(self):
        pass    

    def test_remove_guest_from_room(self):
        self.room4.add_guest_to_room(self.room4, self.tom)
        self.room4.add_guest_to_room(self.room4, self.bert)
        self.room4.add_guest_to_room(self.room4, self.william)
        self.room4.remove_guest_from_room(self.room4, self.tom)
        self.assertEqual(2, self.room4.number_of_guests_in_room(self.room4))

    def test_guests_in_room(self):
        self.assertEqual(0, self.room1.number_of_guests_in_room(self.room1))

    def test_add_song_to_room(self):
        self.room1.add_song_to_room(self.room1, self.new_song)
        self.assertEqual(1, self.room1.number_of_songs_in_room(self.room1))
        self.assertEqual(0, self.room3.number_of_songs_in_room(self.room3))

    def test_get_number_of_songs_in_room(self):
        self.assertEqual(0, self.room2.number_of_songs_in_room(self.room2))
    
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
    
