import pygame

from scripts.functions import load_image
from scripts.variables import cell_size, all_sprites, blocks_breaking, blocks_not_breaking


class Block(pygame.sprite.Sprite):
    image_of_NotBreak = load_image("ntbreak_blokVersion2.png", cell_size, cell_size)
    image_of_Break = load_image("break_block.png", cell_size, cell_size)

    def __init__(self, coords, type):
        super().__init__(all_sprites)
        self.t = ["break", "NotBreak"]
        self.type = type

        self.x, self.y = coords
        if self.t[self.type] == "NotBreak":
            blocks_not_breaking.add(self)
            self.image = Block.image_of_NotBreak
        else:
            self.image = Block.image_of_Break
            self.hp = 1
            blocks_breaking.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, *args):
        pass