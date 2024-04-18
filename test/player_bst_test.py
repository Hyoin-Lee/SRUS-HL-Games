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

        self.assertEqual(bst.root.player.name, player1.name)
        # print (bst.root.player.name)
        self.assertEqual(bst.root.left.player.name, player2.name)
        # print(bst.root.left.player.name)
        self.assertEqual(bst.root.left.right.player.name, player3.name)
        # print(bst.root.left.right.player.name)
        self.assertEqual(bst.root.right.player.name, player4.name)
        # print(bst.root.right.player.name)

    def test_search(self):
        bst = PlayerBST()

        player1 = Player("1", "Scott")
        player2 = Player("2", "Emily")
        player3 = Player("3", "Jin")
        player4 = Player("4", "Ti")

        bst.insert(player1)
        bst.insert(player2)
        bst.insert(player3)
        bst.insert(player4)

        self.assertEqual(bst.search("Scott"), True)
        self.assertEqual(bst.search("Emily"), True)
        self.assertEqual(bst.search("Jin"), True)
        self.assertEqual(bst.search("Ti"), True)
        self.assertEqual(bst.search("Alice"), False)


if __name__ == "__main__":
    unittest.main()
