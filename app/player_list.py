from player_node import PlayerNode
from player import Player
from typing import Optional


class PlayerList:
    def __init__(self):
        self._head: Optional[PlayerNode] = None  # if head is none, list is empty
        self._tail: Optional[PlayerNode] = None

    @property
    def tail(self) -> Optional[PlayerNode]:
        return self._head

    def is_empty(self) -> bool:  # returning boolean value
        return self._head is None

    def insert_at_head(self, player: Player) -> None:
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next_node = self._head
            self._head.prev_node = new_node
            self._head = new_node

    def insert_at_tail(self, player: Player) -> None:
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next_node = new_node
            new_node.prev_node = self._tail
            self._tail = new_node

    def delete_at_head(self) -> Optional[Player]:
        if self.is_empty():  # list is empty
            return None
        elif self._head == self._tail:  # list has only single node
            deleted_player = self._head.player
            self._head = None
            self._tail = None
            return deleted_player
        else:  # list has multiple nodes
            deleted_player = self._head.player
            self._head = self._head.next_node
            self._head.prev_node = None
            return deleted_player

    def delete_at_tail(self) -> Optional[Player]:
        if self.is_empty():  # list is empty
            return None
        elif self._head == self._tail:  # list has only single node
            deleted_player = self._head.player
            self._head = None
            self._tail = None
            return deleted_player
        else:  # list has multiple nodes
            deleted_player = self._tail.player
            self._tail = self._tail.prev_node
            self._tail.next_node = None
            return deleted_player

    def delete_by_key(self, key) -> Optional[Player]:
        current_node = self._head

        if self.is_empty():  # check if list is empty
            return None

        if current_node.player.uid == key:  # check if head node matches the key
            deleted_player = current_node.player
            if self._head == self._tail:
                self._head = None
                self._tail = None
            else:
                self._head = current_node.next_node
                self._head.prev_node = None
            return deleted_player

        while current_node:  # check if any node in the list matches the key and adjust reference before deleting
            if current_node.player.uid == key:
                deleted_player = current_node.player
                if current_node.prev_node:
                    current_node.prev_node.next_node = current_node.next_node
                if current_node.next_node:
                    current_node.next_node.prev_node = current_node.prev_node
                return deleted_player
            current_node = current_node.next_node

        return None  # key not found

    def display(self, forward: bool = True) -> None:
        if forward:
            current_node = self._head
            while current_node:
                print(f"Player: {current_node.player.name} (UID: {current_node.player.uid}) ")
                current_node = current_node.next_node

        else:
            current_node = self._tail
            while current_node:
                print(f"Player: {current_node.player.name} (UID: {current_node.player.uid}) ")
                current_node = current_node.prev_node
