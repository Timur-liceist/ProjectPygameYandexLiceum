from scripts.functions import load_image
from scripts.variables import all_sprites
import pygame
class TextWin(pygame.sprite.Sprite):
    images_wins = [load_image("WinRed.png", 400, 200), load_image("WinBlue.png", 400, 200),
                   load_image("Draw.png", 400, 200)]

    def __init__(self, x, y, player):
        super().__init__(all_sprites)
        player -= 1
        self.image = TextWin.images_wins[player]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        pass