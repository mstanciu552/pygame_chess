import pygame

from Board import Board
from piece_definitions import draw, init

class Game:
    def __init__(self, win):
        self.win = win
        self.board = Board(100)
        self.pieces = init(self.board)
        self.selected = False

    def check_other(self, pieces, piece):
        for p in pieces:
            if pieces[p] == piece:
                continue
            if not pieces[p]:
                return False
        return True

    def check_selected(self):
        for p in self.pieces:
            if self.pieces[p].selected:
                self.selected = self.check_other(self.pieces, self.pieces[p])

    
    def update(self):
        self.board.draw(self.win)
        self.check_selected()
        print(self.selected)
        draw(self.win, self.pieces)
