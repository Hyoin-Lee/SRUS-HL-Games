from player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player):
        self._root = self._insert_recursively(self._root, player)

    def _insert_recursively(self, node, player):
        # If node is None, create a new node with the player and return it
        if node is None:
            return PlayerBNode(player)

        # If the player's name is less than the current node's player name in alphabetical order,
        # insert it into the left subtree
        if player.name < node.player.name:
            node.left = self._insert_recursively(node.left, player)
        # If the player's name is greater than the current node's player name in alphabetically,
        # insert it into the right subtree
        elif player.name > node.player.name:
            node.right = self._insert_recursively(node.right, player)
        # If the player's name is equal to the current node's player name,
        # update the value of the node with the new player object
        else:
            node.player = player

        return node




