class Player:
    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    @classmethod
    def __str__(self):
        return f"Player name is {self.__name} and user ID is {self.__uid}"
