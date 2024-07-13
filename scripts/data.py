import numpy as np
import os
import chess
import chess.pgn
chess_ids = {
    "K": 0,   # Rey blanco
    "Q": 1,   # Reina blanca
    "R": 2,   # Torre blanca
    "B": 3,   # Alfil blanco
    "N": 4,   # Caballo blanco
    "P": 5,   # Peón blanco
    "k": 6,   # Rey negro
    "q": 7,   # Reina negra
    "r": 8,   # Torre negra
    "b": 9,   # Alfil negro
    "n": 10,  # Caballo negro
    "p": 11   # Peón negro
}


def game_isvalid(pgn):
    try:
        game = chess.pgn.read_game(pgn)
        if game:
            return game
        if not game:
            return False
    except UnicodeDecodeError:
        return None

def state_data(board):
    x = np.zeros((14,64))
    # setting positions
    for i in range(64):
        p = board.piece_at(i)
        if p:
            x[chess_ids[p.symbol()]][i] = 1
    lmoves = board.legal_moves
    for m in lmoves:
        x[12][m.to_square] = 1                        
        x[13][m.from_square] = 1
    return x.reshape(14,8,8)

def get_xy():
    fpath = "/kaggle/input/chessdata/Carlsen.pgn"
    inputs = []
    labels = []
    with open(fpath) as pgn:
        while True:
            game = game_isvalid(pgn)
            if game==None:
                continue
            elif not game:
                break
                
            board = game.board()
            for i,move in enumerate(game.mainline_moves()):
                x= state_data(board)
                labels.append(move.uci())
                inputs.append(x)
                board.push(move)

    assert len(inputs) == len(labels)
    return inputs,labels

            

