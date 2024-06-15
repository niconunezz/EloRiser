import pytest
from data_generator import *
class TestClass:
    path = "C:/Users/nicod/OneDrive/Escritorio/Coding/EloRiser/data/Capablanca.pgn"
    boards,res = extract_boards_information(path)

    def test_board_information(self):
        f_boards, f_res = [], []
        board = chess.Board()
        with open(self.path) as pgn:
            game = chess.pgn.read_game(pgn)
            out = game.headers['Result']
            n=0
            for move in game.mainline_moves():
                board.push(move)
                f_boards.append(board)
                f_res.append(score[out])
                n+=1
            
            assert(len(self.boards) == len(self.res))
            assert (f_boards == self.boards[:n])
            assert (f_res == self.res[:n])
    
    def test_x_conversion(self):
        for sq in chess.SQUARES:
            assert(self.boards[17].piece_at(sq) == reverse(get_x_data(self.boards[17])).piece_at(sq))

            
