from player import Player
from typing import Optional


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._next_node: Optional[PlayerNode] = None
        self._previous_node: Optional[PlayerNode] = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def next_node(self) -> Optional['PlayerNode']:
        return self._next_node

    @next_node.setter
    def next_node(self, node: Optional['PlayerNode']) -> None:
        self._next_node = node

    @property
    def prev_node(self) -> Optional['PlayerNode']:
        return self._previous_node

    @prev_node.setter
    def prev_node(self, node: Optional['PlayerNode']) -> None:
        self._previous_node = node

    def key(self) -> str:
        return self._player.uid

    def __str__(self) -> str:
        return f"PlayerNode: {self._player}"
    