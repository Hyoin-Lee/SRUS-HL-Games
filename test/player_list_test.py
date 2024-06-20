import unittest
from player_list import PlayerList
from player import Player


class TestPlayerList(unittest.TestCase):
    def test_insert_at_head_empty_list(self):
        player_list = PlayerList()
        player = Player('35', "Scott")
        player_list.insert_at_head(player)
        self.assertFalse(player_list.is_empty())
        self.assertEqual(player_list._head.player, player)

    def test_insert_at_head_not_empty_list(self):
        player_list = PlayerList()
        player1 = Player('35', "Scott")
        player2 = Player('30', "Emily")
        player_list.insert_at_head(player1)
        player_list.insert_at_head(player2)
        self.assertFalse(player_list.is_empty())
        self.assertEqual(player_list._head.player, player2)
        self.assertEqual(player_list._head.next_node.player, player1)

    def test_insert_at_tail_empty_list(self):
        player_list = PlayerList()
        player = Player('35', "Scott")
        player_list.insert_at_tail(player)
        self.assertFalse(player_list.is_empty())
        self.assertEqual(player_list._tail.player, player)

    def test_insert_at_tail_not_empty_list(self):
        player_list = PlayerList()
        player1 = Player('35', "Scott")
        player2 = Player('30', "Emily")
        player_list.insert_at_tail(player1)
        player_list.insert_at_tail(player2)
        self.assertFalse(player_list.is_empty())
        self.assertEqual(player_list._tail.player, player2)
        self.assertEqual(player_list._tail.prev_node.player, player1)

    def test_delete_at_head_empty_list(self):
        player_list = PlayerList()
        deleted_player = player_list.delete_at_head()
        self.assertIsNone(deleted_player)
        self.assertTrue(player_list.is_empty())

    def test_delete_at_head_not_empty_list(self):
        player_list = PlayerList()
        player1 = Player('35', "Scott")
        player2 = Player('30', "Emily")
        player_list.insert_at_head(player1)
        player_list.insert_at_head(player2)
        deleted_player = player_list.delete_at_head()
        self.assertFalse(player_list.is_empty())
        self.assertEqual(deleted_player, player2)
        self.assertEqual(player_list._head.player, player1)
        self.assertIsNone(player_list._head.prev_node)

    def test_delete_at_tail_empty_list(self):
        player_list = PlayerList()
        deleted_player = player_list.delete_at_tail()
        self.assertIsNone(deleted_player)
        self.assertTrue(player_list.is_empty())

    def test_delete_at_tail_not_empty_list(self):
        player_list = PlayerList()
        player1 = Player('35', "Scott")
        player2 = Player('30', "Emily")
        player_list.insert_at_tail(player1)
        player_list.insert_at_tail(player2)
        deleted_player = player_list.delete_at_tail()
        self.assertFalse(player_list.is_empty())
        self.assertEqual(deleted_player, player2)
        self.assertEqual(player_list._tail.player, player1)
        self.assertIsNone(player_list._tail.next_node)

    def test_delete_by_key_empty_list(self):
        player_list = PlayerList()
        deleted_played = player_list.delete_by_key('35')
        self.assertIsNone(deleted_played)
        self.assertTrue(player_list.is_empty())

    def test_delete_by_key_head(self):
        player_list = PlayerList()
        player1 = Player('35', "Scott")
        player_list.insert_at_head(player1)
        deleted_player = player_list.delete_by_key('35')
        self.assertEqual(deleted_player, player1)
        self.assertTrue(player_list.is_empty())

    def test_delete_by_key_tail(self):
        player_list = PlayerList()
        player1 = Player('35', "Scott")
        player_list.insert_at_tail(player1)
        deleted_player = player_list.delete_by_key('35')
        self.assertEqual(deleted_player, player1)
        self.assertTrue(player_list.is_empty())

    def test_delete_by_key_middle(self):
        player_list = PlayerList()
        player1 = Player('35', "Scott")
        player2 = Player('30', "Emily")
        player3 = Player('25', "Jin")
        player_list.insert_at_head(player1)
        player_list.insert_at_head(player2)
        player_list.insert_at_head(player3)
        deleted_player = player_list.delete_by_key('30')
        self.assertEqual(deleted_player, player2)
        self.assertFalse(player_list.is_empty())
        self.assertEqual(player_list._head.player, player3)
        self.assertEqual(player_list._tail.player, player1)


if __name__ == '__main__':
    unittest.main()
