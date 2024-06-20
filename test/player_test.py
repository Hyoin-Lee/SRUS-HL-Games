import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def test_uid(self):
        player = Player("1", "Scott")
        self.assertEqual(player.uid, "1")

    def test_name(self):
        player = Player("1", "Scott")
        self.assertEqual(player.name, "Scott")

    def test_add_password(self):
        player = Player("1", "Scott")
        plaintext_password = "this is correct password"
        player.add_password(plaintext_password)
        self.assertIsNotNone(player._hash_password)
        self.assertTrue(len(player._hash_password) > 0)

    def test_add_password_raises_error(self):
        player = Player("1", "Scott")
        with self.assertRaises(TypeError):
            player.add_password(123)

    def test_verify_password(self):
        player = Player("1", "Scott")
        plaintext_password = "this is correct password"
        player.add_password(plaintext_password)
        self.assertTrue(player.verify_password(plaintext_password))
        self.assertFalse(player.verify_password("this is not correct password"))

    def test_equal(self):
        player1 = Player(uid='1', name="Scott")
        player2 = Player(uid='2', name="Emily")
        player1.score = 100
        player2.score = 100
        self.assertTrue(player1 == player2)

    def test_not_equal(self):
        player1 = Player(uid='1', name="Scott")
        player2 = Player(uid='2', name="Emily")
        player1.score = 100
        player2.score = 150
        self.assertTrue(player1 != player2)

    def test_less_than(self):
        player1 = Player(uid='1', name="Scott")
        player2 = Player(uid='2', name="Emily")
        player1.score = 100
        player2.score = 150
        self.assertTrue(player1 < player2)

    def test_greater_than(self):
        player1 = Player(uid='1', name="Scott")
        player2 = Player(uid='2', name="Emily")
        player1.score = 150
        player2.score = 100
        self.assertTrue(player1 > player2)

    def test_less_than_or_equal(self):
        player1 = Player(uid='1', name="Scott")
        player2 = Player(uid='2', name="Emily")
        player1.score = 100
        player2.score = 100
        self.assertTrue(player1 <= player2)
        player1.score = 90
        self.assertTrue(player1 <= player2)

    def test_greater_than_or_equal(self):
        player1 = Player(uid='1', name="Scott")
        player2 = Player(uid='2', name="Emily")
        player1.score = 150
        player2.score = 100
        self.assertTrue(player1 >= player2)
        player1.score = 100
        self.assertTrue(player1 >= player2)

    def test_sort_players(self):
        players = [
            Player(uid='1', name="Scott"),
            Player(uid='2', name="Emily"),
            Player(uid='3', name="Jin"),
            Player(uid='4', name="Dave")
        ]
        players[0].score = 100
        players[1].score = 200
        players[2].score = 150
        players[3].score = 50

        Player.sort_players(players)

        expected_order = [200, 150, 100, 50]
        self.assertEqual([player.score for player in players], expected_order)


if __name__ == '__main__':
    unittest.main()
