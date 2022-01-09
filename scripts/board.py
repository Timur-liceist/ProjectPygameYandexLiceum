# from data.levels import level
from scripts.variables import cell_size
from scripts.block import Block
from scripts.grass import Grass
from scripts.functions import load_level
class Board:
    # создание поля
    def __init__(self, width, height, level_for_game):
        self.width = width
        self.height = height
        self.board = load_level(level_for_game)
        self.left = 0
        self.top = 0
        self.cell_size = cell_size
        for w in range(self.width):
            for h in range(self.height):
                x = self.left + w * self.cell_size
                y = self.top + h * self.cell_size
                Grass(w * cell_size, h * cell_size)
                if self.board[h][w] == 1:
                    Block((w * cell_size, h * cell_size), 1)
                if self.board[h][w] == 2:
                    Block((w * cell_size, h * cell_size), 0)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        pass
        # for w in range(self.width):
        #     for h in range(self.height):
        #         x = self.left + w * self.cell_size
        #         y = self.top + h * self.cell_size
        #         if self.board[h][w] == 0:
        #             Grass(w * cell_size, h * cell_size)
        #         if self.board[h][w] == 1:
        #             Block((w * cell_size, h * cell_size), 1)