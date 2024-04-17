from player_bnode import PlayerBNode
from player import Player


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player):
        if not isinstance(player, Player):
            raise TypeError("Argument must be a Player object")

        # If the tree is empty, create a new root node
        if not self._root:
            self._root = PlayerBNode(player)
        else:
            self._insert_recursively(self._root, player)

    def _insert_recursively(self, current_node, player):

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

    def search(self, name):
        return self._search_recursively(self._root, name)

    def _search_recursively(self, current_node, name):
        if current_node is None:
            return False
        if current_node.player.name == name:
            return True
        else:
            if name < current_node.player.name:
                return self._search_recursively(current_node.left, name)
            else:
                return self._search_recursively(current_node.right, name)


# bst = PlayerBST()
#
# bst.insert(Player("1", "Scott"))
# bst.insert(Player("2", "Emily"))
# bst.insert(Player("3", "Jin"))
#
# print (bst.search(name="Scott"))
# print (bst.search(name="Emily"))
# print (bst.search(name="Jin"))
# print (bst.search(name="Ti"))