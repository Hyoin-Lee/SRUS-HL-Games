import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def test_uid(self):
        player = Player("1", "Scott")
        self.assertEqual(player.uid, "1")

    def test_name(self):
        player = Player("1", "Scott")
        self.assertEqual(player.name, "Scott")

if __name__ == '__main__':
    unittest.main()