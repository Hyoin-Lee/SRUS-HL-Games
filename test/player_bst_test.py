import unittest
from player_bst import PlayerBST
from player import Player

class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        self.bst = PlayerBST()

    def test_insert(self):
        self.bst.insert(Player(1, "Scott"))
        self.bst.insert(Player(2, "Emily"))
        self.bst.insert(Player(3, "Jin"))
        self.bst.insert(Player(4, "Ti"))

        self.assertEqual(self.bst.root.player.name, "Scott")  # Root player
        self.assertEqual(self.bst.root.left.player.name, "Emily")  # Left child of root
        self.assertEqual(self.bst.root.left.right.player.name, "Jin")  # Right child of Emily
        self.assertEqual(self.bst.root.right.player.name, "Ti")  # Right child of root

        self.bst.insert(Player(5, "Ti"))
        self.assertEqual(self.bst.root.right.player.uid, 5)  # Updated uid of Ti

if __name__ == "__main__":
    unittest.main()
