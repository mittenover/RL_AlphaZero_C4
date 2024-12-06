import numpy as np
from colorama import Fore, Style, init

# Definition of the class defining the board of the Connect 4 game
#The two players are designated by the numbers 1 and 2. Player 1 is the first to play
#The board is represented by a 6x7 numpy array. The value 0 represents an empty cell, 1 a cell occupied by player 1 and 2 a cell occupied by player 2

class Board:
    def __init__(self):
        self.init_board = np.zeros((6,7))
        self.player = 1
        self.current_board = self.init_board.copy()
        pass

    def play_piece(self, column):
        if self.current_board[0][column] != 0:
            print("Invalid move, the column is full")
            return False
        for i in range(5, -1, -1):
            if self.current_board[i][column] == 0:
                self.current_board[i][column] = self.player
                self.player = 3 - self.player
                break
        return True
    
    def check_winner(self):
        for i in range(6):
            for j in range(7):
                if self.current_board[i][j] != 0:
                    if i < 3:
                        if self.current_board[i][j] == self.current_board[i+1][j] == self.current_board[i+2][j] == self.current_board[i+3][j]:
                            return True
                        if j < 4:
                            if self.current_board[i][j] == self.current_board[i+1][j+1] == self.current_board[i+2][j+2] == self.current_board[i+3][j+3]:
                                return True
                        if j > 2:
                            if self.current_board[i][j] == self.current_board[i+1][j-1] == self.current_board[i+2][j-2] == self.current_board[i+3][j-3]:
                                return True
                    if j < 4:
                        if self.current_board[i][j] == self.current_board[i][j+1] == self.current_board[i][j+2] == self.current_board[i][j+3]:
                            return True
        return False
    
    def print_board(self):
        for row in self.current_board:
            for cell in row:
                if cell == 0:
                    print(Fore.WHITE + '0', end=' ')
                elif cell == 1:
                    print(Fore.RED + '1', end=' ')
                elif cell == 2:
                    print(Fore.YELLOW + '2', end=' ')
            print(Style.RESET_ALL)  # Reset color after each row
    
    def all_actions(self):
        actions = []
        for i in range(7):
            if self.current_board[0][i] == 0:
                actions.append(i)
        return actions
    
