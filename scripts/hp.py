import pygame
from scripts.functions import load_image
from scripts.variables import all_sprites
class Heart(pygame.sprite.Sprite):
    images_of_heart = [load_image("HpBlue.png", 30, 30), load_image("HpRed.png", 30, 30)]

    def __init__(self, x, y, player):
        super().__init__(all_sprites)
        self.image = Heart.images_of_heart[player - 1]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, args):
        pass


class Hp:

    def __init__(self, x, y, player, hp):
        self.hp = hp
        self.color = ["Blue", "Red"][player - 1]
        self.x, self.y = x, y
        self.hearts = []
        for i in range(self.hp):
            heart = Heart(x, y, player)
            x += 15
            self.hearts.append(heart)

    def update_hp(self):
        self.hp -= 1
        if self.hearts:
            self.hearts[-1].kill()
            del self.hearts[-1]