from Piece import Piece

def init(board):
    # WHITE
    white_pawn1 = Piece((0, 1), 1, board, './images/white_pawn.png')
    white_pawn2 = Piece((1, 1), 1, board, './images/white_pawn.png')
    white_pawn3 = Piece((2, 1), 1, board, './images/white_pawn.png')
    white_pawn4 = Piece((3, 1), 1, board, './images/white_pawn.png')
    white_pawn5 = Piece((4, 1), 1, board, './images/white_pawn.png')
    white_pawn6 = Piece((5, 1), 1, board, './images/white_pawn.png')
    white_pawn7 = Piece((6, 1), 1, board, './images/white_pawn.png')
    white_pawn8 = Piece((7, 1), 1, board, './images/white_pawn.png')
    
    white_bishop1 = Piece((2, 0), 1, board, './images/white_bishop.png')
    white_bishop2 = Piece((5, 0), 1, board, './images/white_bishop.png')
    
    white_knight1 = Piece((1, 0), 1, board, './images/white_knight.png')
    white_knight2 = Piece((6, 0), 1, board, './images/white_knight.png')
    
    white_rook1 = Piece((0, 0), 1, board, './images/white_rook.png')
    white_rook2 = Piece((7, 0), 1, board, './images/white_rook.png')
    
    white_queen = Piece((3, 0), 1, board, './images/white_queen.png')
    white_king = Piece((4, 0), 1, board, './images/white_king.png')
    
    #BLACK
    black_pawn1 = Piece((0, 6), 1, board, './images/black_pawn.png')
    black_pawn2 = Piece((1, 6), 1, board, './images/black_pawn.png')
    black_pawn3 = Piece((2, 6), 1, board, './images/black_pawn.png')
    black_pawn4 = Piece((3, 6), 1, board, './images/black_pawn.png')
    black_pawn5 = Piece((4, 6), 1, board, './images/black_pawn.png')
    black_pawn6 = Piece((5, 6), 1, board, './images/black_pawn.png')
    black_pawn7 = Piece((6, 6), 1, board, './images/black_pawn.png')
    black_pawn8 = Piece((7, 6), 1, board, './images/black_pawn.png')
    
    black_bishop1 = Piece((2, 7), 1, board, './images/black_bishop.png')
    black_bishop2 = Piece((5, 7), 1, board, './images/black_bishop.png')
    
    black_knight1 = Piece((1, 7), 1, board, './images/black_knight.png')
    black_knight2 = Piece((6, 7), 1, board, './images/black_knight.png')
    
    black_rook1 = Piece((7, 7), 1, board, './images/black_rook.png')
    black_rook2 = Piece((0, 7), 1, board, './images/black_rook.png')
    
    black_queen = Piece((3, 7), 1, board, './images/black_queen.png')
    black_king = Piece((4, 7), 1, board, './images/black_king.png')

    return {
        'white_pawn1': white_pawn1,
        'white_pawn2': white_pawn2,
        'white_pawn3': white_pawn3,
        'white_pawn4': white_pawn4,
        'white_pawn5': white_pawn5,
        'white_pawn6': white_pawn6,
        'white_pawn7': white_pawn7,
        'white_pawn8': white_pawn8,
        'white_rook1': white_rook1,
        'white_rook2': white_rook2,
        'white_bishop1': white_bishop1,
        'white_bishop2': white_bishop2,
        'white_knight1': white_knight1,
        'white_knight2': white_knight2,
        'white_queen': white_queen,
        'white_king': white_king,

        'black_pawn1': black_pawn1,
        'black_pawn2': black_pawn2,
        'black_pawn3': black_pawn3,
        'black_pawn4': black_pawn4,
        'black_pawn5': black_pawn5,
        'black_pawn6': black_pawn6,
        'black_pawn7': black_pawn7,
        'black_pawn8': black_pawn8,
        'black_rook1': black_rook1,
        'black_rook2': black_rook2,
        'black_bishop1': black_bishop1,
        'black_bishop2': black_bishop2,
        'black_knight1': black_knight1,
        'black_knight2': black_knight2,
        'black_queen': black_queen,
        'black_king': black_king,
    }


def draw(win, pieces):
    for piece in pieces:
        pieces[piece].update(win)
