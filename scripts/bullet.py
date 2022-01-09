from scripts.variables import bullets_of_player2, bullets_of_player1, all_sprites, cell_size
import pygame
from scripts.functions import load_image
class Bullet(pygame.sprite.Sprite):
    image_of_bullet = load_image("bullet.png", 20, 20)

    def __init__(self, x, y, vx, vy, player):
        super().__init__(all_sprites)
        self.image = Bullet.image_of_bullet
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.x, self.y = x, y
        self.vx = vx
        self.vy = vy
        self.mask = pygame.mask.from_surface(self.image)
        self.player = player
        if player == 1:
            bullets_of_player1.add(self)
        if player == 2:
            bullets_of_player2.add(self)

    def update(self, *args):
        self.rect.x += self.vx
        self.rect.y += self.vy
        # if pygame.sprite.collide_mask(self, tank1) and self.player == 2:
        #     tank1.hp -= 1
        #     hp_tank1.update_hp()
        #     self.kill()
        #     if tank1.hp == 0:
        #         podchet_scoreRed.score += 1
        #     if tank1.hp > 0:
        #         pygame.mixer.music.load('data/probitie.mp3')
        #         pygame.mixer.music.play()
        #     AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
        #     return
        # elif pygame.sprite.collide_mask(self, tank2) and self.player == 1:
        #     tank2.hp -= 1
        #     self.kill()
        #     hp_tank2.update_hp()
        #     if tank2.hp > 0:
        #         pygame.mixer.music.load('data/probitie.mp3')
        #         pygame.mixer.music.play()
        #     if tank2.hp == 0:
        #         podchet_scoreBlue.score += 1
        #     AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
        #     return
        # if self.player == 1:
        #     for i in bullets_of_player2:
        #         if pygame.sprite.collide_mask(self, i):
        #             self.kill()
        #             i.kill()
        #             AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
        #             return
        # elif self.player == 2:
        #     for i in bullets_of_player1:
        #         if pygame.sprite.collide_mask(self, i):
        #             self.kill()
        #             AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
        #             i.kill()
        #             return
        # for i in blocks_not_breaking:
        #     if pygame.sprite.collide_mask(self, i):
        #         self.kill()
        #         AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
        #         return
        # for i in blocks_breaking:
        #     if pygame.sprite.collide_mask(self, i):
        #         self.kill()
        #         AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
        #         i.kill()
        #         return
        # if pygame.sprite.collide_mask(self, base1):
        #     base1.hp -= 1
        #     AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
        #     self.kill()
        #     base1_hp.update_hp()
        # if pygame.sprite.collide_mask(self, base2):
        #     base2.hp -= 1
        #     base2_hp.update_hp()
        #     AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
        #     self.kill()
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if self.cur_frame == 0:
            self.kill()