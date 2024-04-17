import unittest
from player_bst import PlayerBST
from player import Player

class TestPlayerBST(unittest.TestCase):
    def test_insert(self):
        bst = PlayerBST()

        player1 = Player("1", "Scott")
        player2 = Player("2", "Emily")
        player3 = Player("3", "Jin")
        player4 = Player("4", "Ti")

        bst.insert(player1)
        bst.insert(player2)
        bst.insert(player3)
        bst.insert(player4)

        self.assertEqual(bst.root.player, player1)   # Root player = Scott
        self.assertEqual(bst.root.left.player, player2)  # Left child of root = Emily
        self.assertEqual(bst.root.left.right.player, player3)  # Right child of Emily
        self.assertEqual(bst.root.right.player, player4)  # Right child of root



if __name__ == "__main__":
    unittest.main()
