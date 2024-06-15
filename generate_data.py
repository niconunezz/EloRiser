import numpy as np
import chess
import os
import chess.pgn
chess_ids= {
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
reversed_chess_ids = {v:i for i,v in chess_ids.items()}
score = {"1-0":1,"1/2-1/2":0,"0-1":-1}
def extract_boards_information(path):
    boards = []
    res = []
    with open(path) as pgn:
        while True:
            game = chess.pgn.read_game(pgn)
            if not game:
                break
            out = game.headers['Result']
            if out == "*":
                continue
            result = score[out]
            board = game.board()
            for move in game.mainline_moves():
                board.push(move)
                boards.append(board)
                res.append(result)
    return boards,res
def get_x_data(board):
    row = [0 for i in range(64)]
    for i in range(64):
        pp = board.piece_at(i)
        if pp!=None:
            pp = pp.symbol()
            row[i] = [0 for i in range(12)]
            row[i][chess_ids[pp]] = 1
        else:
            row[i] = [0 for i in range(12)]
    return np.array(row).reshape(8,8,12)
def get_xy_data(boards,res):
    x = []
    y = []
    for i in range(len(boards)):
        x_data = get_x_data(boards[i])
        x.append(x_data)
        y.append(res[i])
    assert(len(x) == len(y))
    return x,y


def get_data(data):
    x_data = []
    y_data = []
    i=0
    for f in data:
        path = f'data/{f}'
        boards,res = extract_boards_information(path)
        x,y = get_xy_data(boards,res)
        x_data.extend(x)
        y_data.extend(y)
        i+=1
        print(f"{i}/{len(data)}")
        break
    x_data = np.array(x_data)
    y_data = np.array(y_data)
    return x_data,y_data

def generate():
    data = os.listdir("data")
    x,y = get_data(data)
    return x,y

def reverse(x):
    board = chess.Board()
    for square in chess.SQUARES:

        board.remove_piece_at(square)      
        for k in range(12):
            if x[square//8][square%8][k]==1:
                piece = reversed_chess_ids[k]
                board.set_piece_at(square, chess.Piece.from_symbol(piece))
    
    return(board)