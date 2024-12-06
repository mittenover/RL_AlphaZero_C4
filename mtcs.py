import numpy as np

class node:
    """
    A class used to represent a node in the Monte Carlo Tree Search algorithm

    ...

    Attributes
    ----------
    Methods
    ------- 
    ifterminal()
        Check if the node is terminal
    ifleaf()
        Check if the node is a leaf
    """

    def __init__(self, board, action, parent=None):
        self.parent = parent 
        self.children = []
        self.board = board #The board state of the node (of board class)
        self.action = action #The action that led to this node
        self.n = 0 #Number of visits
        self.w = 0 #Total value of the node
        self.q = 0 #Average value of the node

        def ifterminal(self):
            return(self.board.check_winner() or len(self.board.all_actions()) == 0)
        
        def ifleaf(self):
            return(len(self.children) == 0)
        
class mtcs:
    """
    A class used to represent the Monte Carlo Tree Search algorithm

    ...

    Attributes
    ----------
    Methods
    ------- 
    """