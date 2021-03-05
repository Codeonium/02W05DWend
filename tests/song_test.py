import unittest

from classes.song import Song


class TestSong(unittest.TestCase):
        def setUp(self):
            self.take_on_me = Song("Take On Me", "80's", 1.50, 244)

        def test_has_name(self):
            self.assertEqual("Take On Me", self.take_on_me.title)
        
        def test_has_decade(self):
            self.assertEqual("80's", self.take_on_me.decade)

        def test_has_price(self):
            self.assertEqual(1.50, self.take_on_me.price)
        
        def test_has_time_in_seconds(self):
            self.assertEqual(244, self.take_on_me.duration)

# No more changes here to be made