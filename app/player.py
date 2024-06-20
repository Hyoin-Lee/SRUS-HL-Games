from argon2 import PasswordHasher


class Player:
    def __init__(self, uid: str, name: str) -> None:
        self._uid: str = uid
        self._name: str = name
        self._hash_password: str = ""
        self.ph = PasswordHasher()
        self.score: int = 0

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Score must be an integer")
        if value < 0:
            raise ValueError("Score must be a positive integer")
        self._score = value

    @classmethod
    def __str__(self) -> str:
        return f"Player name is {self._name} and user ID is {self._uid}"

    def add_password(self, plaintext_password: str) -> None:
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
    def _partition(players: list['Player'], low: int, high: int) -> int:
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
    def _quick_sort(players: list['Player'], low: int, high: int) -> None:
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
    def sort_players(players: list['Player']) -> None:
        Player._quick_sort(players, 0, len(players) - 1)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self.score == other.score

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self.score != other.score

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self.score < other.score

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self.score <= other.score

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self.score > other.score

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self.score >= other.score
