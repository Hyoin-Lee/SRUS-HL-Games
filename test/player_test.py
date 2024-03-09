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



if __name__ == '__main__':
    unittest.main()
