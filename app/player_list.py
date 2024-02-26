from player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.__head = None  # if head is none, list is empty
        self.__tail = None

    @property
    def tail(self):
        return self.__head

    def is_empty(self):  # returning boolean value
        return self.__head is None

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
        if self.is_empty():  # list is empty
            return None
        elif self.__head == self.__tail:  # list has only single node
            self.__head = None
            self.__tail = None
        else:  # list has multiple nodes
            deleted_player = self.__head.player
            self.__head = self.__head.next_node
            self.__head.prev_node = None
            return deleted_player

    def delete_at_tail(self):
        if self.is_empty():  # list is empty
            return None
        elif self.__head == self.__tail:  # list has only single node
            self.__head = None
            self.__tail = None
        else:  # list has multiple nodes
            deleted_player = self.__tail.player
            self.__tail = self.__tail.prev_node
            self.__tail.next_node = None
            return deleted_player

    def delete_by_key(self, key):
        current_node = self.__head

        if self.is_empty():  # check if list is empty
            return None

        if current_node.player.uid == key:  # check if head node matches the key
            deleted_player = current_node.player
            if self.__head == self.__tail:
                self.__head = None
                self.__tail = None
            else:
                self.__head = current_node.next_node
                self.__head.prev_node = None
            return deleted_player

        while current_node:  # check if any node in the list matches the key and adjust reference before deleting
            if current_node.player.uid == key:
                deleted_player = current_node.player
                current_node.prev_node.next_node = current_node.next_node
                current_node.next_node.prev_node = current_node.prev_node
                return deleted_player
            current_node = current_node.next_node

        return None  # key not found

