import unittest
from app.player_list import PlayerList
from app.player import Player


class TestPlayerList(unittest.TestCase):
    def test_insert_at_head_empty_list(self):
        player_list = PlayerList()
        player = Player(35, "Scott")
        player_list.insert_at_head(player)
        self.assertFalse(player_list.is_empty())
        self.assertEqual(player_list._PlayerList__head.player, player)

    def test_insert_at_head_not_empty_list(self):
        player_list = PlayerList()
        player1 = Player(35, "Scott")
        player2 = Player(30, "Emily")
        player_list.insert_at_head(player1)
        player_list.insert_at_head(player2)
        self.assertFalse(player_list.is_empty())
        self.assertEqual(player_list._PlayerList__head.player, player2)
        self.assertEqual(player_list._PlayerList__head.next_node.player, player1)

    def test_insert_at_tail_empty_list(self):
        player_list = PlayerList()
        player = Player(35, "Scott")
        player_list.insert_at_tail(player)
        self.assertFalse(player_list.is_empty())
        self.assertEqual(player_list._PlayerList__tail.player, player)

    def test_insert_at_tail_not_empty_list(self):
        player_list = PlayerList()
        player1 = Player(35, "Scott")
        player2 = Player(30, "Emily")
        player_list.insert_at_tail(player1)
        player_list.insert_at_tail(player2)
        self.assertFalse(player_list.is_empty())
        self.assertEqual(player_list._PlayerList__tail.player, player2)
        self.assertEqual(player_list._PlayerList__tail.prev_node.player, player1)

    def test_delete_at_head_empty_list(self):

    def test_delete_at_head_not_empty_list(self):

    def test_delete_at_tail_empty_list(self):

    def test_delete_at_tail_not_empty_list(self):



if __name__ == '__main__':
    unittest.main()
