from player_bnode import PlayerBNode
from player import Player
from typing import List, Optional


class PlayerBST:
    def __init__(self) -> None:
        self._root: Optional[PlayerBNode] = None
        self._sorted_list: List[Player] = []

    @property
    def root(self) -> Optional[PlayerBNode]:
        return self._root

    def insert(self, player: Player) -> None:
        if not isinstance(player, Player):
            raise TypeError("Argument must be a Player object")

        # If the tree is empty, create a new root node
        if not self._root:
            self._root = PlayerBNode(player)
        else:
            self._insert_recursively(self._root, player)

    def _insert_recursively(self, current_node: PlayerBNode, player) -> None:
        # If the player's name is less than the current node's player name in alphabetical order,
        # insert it into the left subtree
        if player.name < current_node.player.name:
            # If the left child of the current node exists, it calls _insert_recursively to insert
            # the player object into the right position
            if current_node.left:
                self._insert_recursively(current_node.left, player)
            # If it doesn't exist, it creates a new PlayerBNode with the player object and sets it
            # as the left child of the current node
            else:
                current_node.left = PlayerBNode(player)

        # If the player's name is greater than the current node's player name in alphabetically,
        # insert it into the right subtree
        elif player.name > current_node.player.name:
            # If the right child of the current node exists, it calls _insert_recursively to insert
            # the player object into the right position
            if current_node.right:
                self._insert_recursively(current_node.right, player)
            # If it doesn't exist, it creates a new PlayerBNode with the player object and sets it
            # as the right child of the current node
            else:
                current_node.right = PlayerBNode(player)
        # If the player's name is equal to the current node's player name,
        # update the player object
        else:
            current_node.player = player

    def search(self, name: str) -> bool:
        return self._search_recursively(self._root, name)

    def _search_recursively(self, current_node: Optional[PlayerBNode], name: str) -> bool:
        if current_node is None:
            return False
        if current_node.player.name == name:
            return True
        else:
            if name < current_node.player.name:
                return self._search_recursively(current_node.left, name)
            else:
                return self._search_recursively(current_node.right, name)

    def in_order_traverse(self) -> List[Player]:
        self._sorted_list = []
        self._in_order_traverse_recursively(self._root)
        return self._sorted_list

    def _in_order_traverse_recursively(self, current_node: Optional[PlayerBNode]) -> None:
        if current_node:
            self._in_order_traverse_recursively(current_node.left)
            self._sorted_list.append(current_node.player)
            self._in_order_traverse_recursively(current_node.right)

    def construct_balanced_bst(self) -> None:
        players_sorted = self.in_order_traverse()
        return self._construct_balanced_bst_recursively(players_sorted)

    def _construct_balanced_bst_recursively(self, players: List[Player]) -> Optional[PlayerBNode]:
        if not players:
            return None
        middle_element = len(players) // 2
        root = PlayerBNode(players[middle_element])
        root.left = self._construct_balanced_bst_recursively(players[:middle_element])
        root.right = self._construct_balanced_bst_recursively(players[middle_element+1:])
        return root


bst = PlayerBST()
bst.insert(Player("1", "Scott"))
bst.insert(Player("2", "Emily"))
bst.insert(Player("3", "Jin"))
bst.insert(Player("4", "Alice"))
bst.insert(Player("5", "Grace"))
bst.insert(Player("6", "Bob"))
bst.insert(Player("7", "Dan"))

sorted_players = bst.in_order_traverse()
print("Sorted list of players:", [player.name for player in sorted_players])

bst.construct_balanced_bst()

sorted_players_balanced = bst.in_order_traverse()
print("Sorted list of players in balanced BST:", [player.name for player in sorted_players_balanced])
