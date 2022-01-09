from scripts.variables import all_sprites, HP_TANKS, blocks_breaking, blocks_not_breaking
from scripts.functions import load_image
import pygame
from scripts.variables import cell_size
class Tank(pygame.sprite.Sprite):
    image_of_tank = [load_image("tankBlue.png"),
                     load_image("tankRed.png")]

    def __init__(self, x, y, player):
        super().__init__(all_sprites)
        self.image = Tank.image_of_tank[player]
        self.rect = self.image.get_rect()
        self.image_of_tank = Tank.image_of_tank[player]
        self.rect.x = x
        self.rect.y = y
        self.hp = HP_TANKS
        self.x, self.y = x, y
        self.music_tank_unich = True
        self.gradus = 180
        self.mask = pygame.mask.from_surface(self.image)

    # def shoot(self, x, y, vx, vy):
    #     pass
    def move(self, x, y):
        if self.hp > 0:
            tx = self.x
            ty = self.y
            if x != self.x and y != self.y:
                return
            if x > self.x:
                self.image = pygame.transform.rotate(self.image_of_tank, 270)
                self.gradus = 270
            if x < self.x:
                self.image = pygame.transform.rotate(self.image_of_tank, 90)
                self.gradus = 90
            if y > self.y:
                self.image = pygame.transform.rotate(self.image_of_tank, 180)
                self.gradus = 180
            if y < self.y:
                self.image = self.image_of_tank
            self.rect.x = x
            self.rect.y = y
            self.x = x
            self.y = y
            for i in blocks_not_breaking:
                if pygame.sprite.collide_mask(self, i):
                    self.rect.x = tx
                    self.rect.y = ty
                    self.x = tx
                    self.y = ty
            for i in blocks_breaking:
                if pygame.sprite.collide_mask(self, i):
                    self.rect.x = tx
                    self.rect.y = ty
                    self.x = tx
                    self.y = ty

    def update(self, *args):
        if self.hp == 0 and self.music_tank_unich:
            pygame.mixer.music.load('../data/tank-unichtozhen.mp3')
            pygame.mixer.music.play()
            self.music_tank_unich = False
            self.image = pygame.transform.rotate(load_image("tankMinus.png", cell_size, cell_size), self.gradus)
            # terminate()