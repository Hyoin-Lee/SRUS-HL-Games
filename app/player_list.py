from .player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.__head = None
    '''
    if head is none, list is empty
    if not, list is not empty 
    '''

    def is_empty(self):
        return self.__head is None
    '''
    returning boolean value 
    '''

    def insert_at_head(self, player):
        new_node = PlayerNode(player)
        if self.is_empty():
            self.__head = new_node
        else:
            new_node.next_node = self.__head
            self.__head.prev_node = new_node
            self.__head = new_node
