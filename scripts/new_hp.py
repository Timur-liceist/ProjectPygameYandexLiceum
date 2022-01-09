import pygame
from scripts.functions import load_image
from random import randrange
from scripts.variables import all_sprites
class BoxWithHp(pygame.sprite.Sprite):
    image_of_box = load_image("box_with_hp.png")
    def __init__(self, board):
        super().__init__(all_sprites)
        self.image = BoxWithHp.image_of_box
        self.rect = self.image.get_rect()
        random_i, random_j = randrange(1, 25), randrange(1, 25)
        while board.board[random_i][random_j] != 0:
            random_i, random_j = randrange(1, 25), randrange(1, 25)
        self.rect.y = random_i * 20
        self.rect.x = random_j * 20
        self.mask = pygame.mask.from_surface(self.image)
        # self.rect.y = 10
        # self.rect.x = 10
