from argon2 import PasswordHasher


class Player:
    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name
        self._hash_password = None
        self.ph = PasswordHasher()

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    @classmethod
    def __str__(self):
        return f"Player name is {self.__name} and user ID is {self.__uid}"

    def add_password(self, plaintext_password):
        if not isinstance(plaintext_password, str):
            raise TypeError("Password must be string")
        self._hash_password = self.ph.hash(plaintext_password)

    def verify_password(self, plaintext_password):
        try:
            self.ph.verify(self._hash_password, plaintext_password)
            return True
        except Exception:
            return False