import pygame
from scripts.functions import load_image
from scripts.variables import cell_size, all_sprites
class Grass(pygame.sprite.Sprite):
    image_of_grass = load_image("grass.jpg", cell_size, cell_size)

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Grass.image_of_grass
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        pass