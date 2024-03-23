from argon2 import PasswordHasher


class Player:
    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name
        self._hash_password = None
        self.ph = PasswordHasher()
        self.score = 0

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise TypeError("Score must be an integer")
        if value < 0:
            raise ValueError("Score must be a positive integer")
        self._score = value

    @classmethod
    def __str__(cls):
        return f"Player name is {cls.__name} and user ID is {cls.__uid}"

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

    @staticmethod
    # function to find the partition position
    def _partition(players, low, high):
        # choose the rightmost element as pivot
        pivot = players[high]
        # pointer for greater element
        i = low - 1
        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if players[j] >= pivot:
                # if element smaller than pivot is found
                # swap it with the greater element pointed by i
                i += 1
                # swapping element at i with element at j
                players[i], players[j] = players[j], players[i]
                # swap the pivot element with greater element specified by i
        players[i + 1], players[high] = players[high], players[i + 1]
        # return the position from where partition is done
        return i + 1

    @staticmethod
    # function to perform quicksort
    def _quick_sort(players, low, high):
        if low < high:

            # find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pivot_index = Player._partition(players, low, high)

            # recursive call on the left of pivot
            Player._quick_sort(players, low, pivot_index - 1)

            # recursive call on the right of pivot
            Player._quick_sort(players, pivot_index + 1, high)

    @staticmethod
    def sort_players(players):
        Player._quick_sort(players, 0, len(players) - 1)


    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.score == other.score

    def __ne__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.score != other.score

    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.score < other.score

    def __le__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.score <= other.score

    def __gt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.score > other.score

    def __ge__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.score >= other.score


