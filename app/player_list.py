from .player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.__head = None  #if head is none, list is empty
        self.__tail = None

    @property
    def tail(self):
        return self.__head

    def is_empty(self):
        return self.__head is None
    '''
    returning boolean value 
    '''

    def insert_at_head(self, player):
        new_node = PlayerNode(player)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next_node = self.__head
            self.__head.prev_node = new_node
            self.__head = new_node

    def insert_at_tail(self, player):
        new_node = PlayerNode(player)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next_node = new_node
            new_node.prev_node = self.__tail
            self.__tail = new_node

    def delete_at_head(self):
        if self.is_empty(): #list is empty
            return None
        elif self.__head == self.__tail: #list has only one node
            self.__head = None
            self.__tail = None
        else:
            deleted_player = self.__head.player
            self.__head = self.__head.next_node
            self.__head.prev.node = None
        return deleted_player

    def delete_at_tail(self):
        if self.is_empty():
            return None
        elif self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            deleted_player = self.__tail.player
            self.__tail = self.tail.prev.node
            self.__tail.next.node = None
        return deleted_player




