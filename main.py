from board import Board
import numpy as np

if __name__ =='__main__':

    #Board test
    board = Board()

    board.play_piece(0)
    board.print_board()
    
    board.play_piece(0)
    board.print_board()
    
    board.play_piece(0)
    board.print_board()
    
    board.play_piece(2)
    board.print_board()
    
    board.play_piece(0)
    board.print_board()
    
    board.play_piece(1)
    board.print_board()
    
    board.play_piece(0)
    board.print_board()
    
    board.play_piece(1)
    board.print_board()

    board.play_piece(0)
    board.print_board()
    print(board.check_winner())
    