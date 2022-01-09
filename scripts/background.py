import pygame
from scripts.variables_for_menu import all_sprites
from scripts.functions import load_image
class Background(pygame.sprite.Sprite):
    image_of_background = load_image("background_for_menu.jpg", 720, 500)
    def __init__(self):
        super().__init__(all_sprites)
        self.image = Background.image_of_background
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    def update(self):
        pass