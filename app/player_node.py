class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__next_node = None
        self.__previous_node = None

    @property
    def player(self):
        return self.__player

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        self.__next_node = node

    @property
    def prev_node(self):
        return self.__previous_node

    @prev_node.setter
    def prev_node(self, node):
        self.__previous_node = node

    def key(self):
        return self.__player.uid

    def __str__(self):
        return f"PlayerNode: {self.__player}"