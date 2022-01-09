from scripts.functions import load_image
import pygame
from scripts.variables import all_sprites, HP_BASE, cell_size
class Base(pygame.sprite.Sprite):
    image_of_base = [load_image("base1.png", cell_size, cell_size), load_image("base2.png", cell_size, cell_size)]

    def __init__(self, x, y, player):
        super().__init__(all_sprites)
        self.image = Base.image_of_base[player - 1]
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.hp = HP_BASE