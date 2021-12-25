import pygame
import os
import sys

from PyQt5 import QtMultimedia, QtCore

from data.level import level
import random

all_sprites = pygame.sprite.Group()
cell_size = 20
blocks_not_breaking = pygame.sprite.Group()
blocks_breaking = pygame.sprite.Group()
bullets_of_player1 = pygame.sprite.Group()
bullets_of_player2 = pygame.sprite.Group()
EVENT_PERESAR_TANK1 = 30
EVENT_PERESAR_TANK2 = 60
class Score:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.score = 0
        self.color = color
    def render(self):
        font = pygame.font.Font(None, 50)
        text = font.render(f"{self.score}", True, self.color)
        # text_x = width // 2 - text.get_width() // 2
        # text_y = height // 2 - text.get_height() // 2
        text_x = self.x
        text_y = self.y
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, self.color, (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
podchet_scoreBlue = Score(515, 15, "blue")
podchet_scoreRed = Score(570, 15, "red")


def load_image(name, w=None, h=None, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        try:
            # image = image.convert_alpha()
            image = image.convert()
        except Exception:
            pass
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        try:
            image = image.convert_alpha()
        except Exception:
            pass
    if w and h:
        image = pygame.transform.scale(image, (w, h))
    return image


def terminate():
    pygame.quit()
    sys.exit()


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


class Base(pygame.sprite.Sprite):
    image_of_base = [load_image("base1.png", cell_size, cell_size), load_image("base2.png", cell_size, cell_size)]

    def __init__(self, x, y, player):
        super().__init__(all_sprites)
        self.image = Base.image_of_base[player - 1]
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = level.copy()
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
        if pygame.sprite.collide_mask(self, tank1) and self.player == 2:
            tank1.hp -= 1
            self.kill()
            pygame.mixer.music.load('data/probitie.mp3')
            pygame.mixer.music.play()
            AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
            return
        elif pygame.sprite.collide_mask(self, tank2) and self.player == 1:
            tank2.hp -= 1
            self.kill()
            pygame.mixer.music.load('data/probitie.mp3')
            pygame.mixer.music.play()
            AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
            return
        if self.player == 1:
            for i in bullets_of_player2:
                if pygame.sprite.collide_mask(self, i):
                    self.kill()
                    i.kill()
                    AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
                    return
        elif self.player == 2:
            for i in bullets_of_player1:
                if pygame.sprite.collide_mask(self, i):
                    self.kill()
                    AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
                    i.kill()
                    return
        for i in blocks_not_breaking:
            if pygame.sprite.collide_mask(self, i):
                self.kill()
                AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
                return
        for i in blocks_breaking:
            if pygame.sprite.collide_mask(self, i):
                self.kill()
                AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, self.rect.x, self.rect.y)
                i.kill()
                return
class Tank(pygame.sprite.Sprite):
    image_of_tank = [load_image("tankBlue.png", cell_size, cell_size, -1),
                     load_image("tankRed.png", cell_size, cell_size, -1)]

    def __init__(self, x, y, player):
        super().__init__(all_sprites)
        self.image = Tank.image_of_tank[player]
        self.rect = self.image.get_rect()
        self.image_of_tank = Tank.image_of_tank[player]
        self.rect.x = x
        self.rect.y = y
        self.hp = 2
        self.x, self.y = x, y
        self.music_tank_unich = True
        self.gradus = 180
        self.mask = pygame.mask.from_surface(self.image)

    # def shoot(self, x, y, vx, vy):
    #     pass
    def move(self, x, y):
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
            print(1)
            pygame.mixer.music.load('data/tank-unichtozhen.mp3')
            pygame.mixer.music.play()
            self.music_tank_unich = False
            self.image = pygame.transform.rotate(load_image("tankMinus.png", cell_size, cell_size), self.gradus)
            # terminate()


GRAVITY = 0.1
screen_rect = (0, 0, 500, 500)


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self, *args):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


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


pygame.display.set_caption('Танчики')
screen = pygame.display.set_mode((700, 500))
playground = Board(25, 25)
base1 = Base(12 * cell_size, 1 * cell_size, 1)
base2 = Base(12 * cell_size, (25 - 2) * cell_size, 2)
fps = 30  # количество кадров в секунду
clock = pygame.time.Clock()
running = True
go_tank1 = False
dx_tank1 = 0
dy_tank1 = 0
go_tank2 = False
dx_tank2 = 0
dy_tank2 = 0
step = 1.7
step_bullet = 10
bullet_dx_tank1 = 0
bullet_dy_tank1 = step
bullet_dx_tank2 = 0
bullet_dy_tank2 = -step
play = True
ready_vistrel_tank1 = True
ready_vistrel_tank2 = True
time_peresaryadky = 800
pygame.time.set_timer(EVENT_PERESAR_TANK1, time_peresaryadky)
pygame.time.set_timer(EVENT_PERESAR_TANK2, time_peresaryadky)
for i in range(playground.height):
    for j in range(playground.width):
        if playground.board[i][j] == 4:
            tank2 = Tank(j * cell_size, i * cell_size, 1)
        if playground.board[i][j] == 3:
            tank1 = Tank(j * cell_size, i * cell_size, 0)
tank1.image = pygame.transform.rotate(tank1.image_of_tank, 180)

pygame.init()
# playing_music_of_tank_unichtozhen = True
while running:

    if (tank1.hp == 0 or tank2.hp == 0) and play:
        # if playing_music_of_tank_unichtozhen:
        #     playing_music_of_tank_unichtozhen = False
        create_particles((100, 100))
        create_particles((400, 100))
        create_particles((400, 400))
        create_particles((100, 400))
        create_particles((225, 250))
        create_particles((250, 250))
        play = False
    if play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # player1
                if event.key == pygame.K_w:  # Обработка клавици "w"
                    dy_tank1 = -step
                    bullet_dy_tank1 = -step_bullet
                    bullet_dx_tank1 = 0
                    go_tank1 = True
                if event.key == pygame.K_s:  # Обработка клавици "w"
                    dy_tank1 = step
                    bullet_dy_tank1 = step_bullet
                    bullet_dx_tank1 = 0
                    go_tank1 = True
                if event.key == pygame.K_a:  # Обработка клавици "w"
                    dx_tank1 = -step
                    bullet_dx_tank1 = -step_bullet
                    bullet_dy_tank1 = 0
                    go_tank1 = True
                if event.key == pygame.K_d:  # Обработка клавици "w"
                    dx_tank1 = step
                    bullet_dx_tank1 = step_bullet
                    bullet_dy_tank1 = 0
                    go_tank1 = True
                if event.key == pygame.K_SPACE:
                    if ready_vistrel_tank1:
                        Bullet(tank1.x, tank1.y, bullet_dx_tank1, bullet_dy_tank1, 1)
                        pygame.mixer.music.load('data/zvuk_shoot (mp3cut.net).mp3')
                        pygame.mixer.music.play()
                        pygame.time.set_timer(EVENT_PERESAR_TANK1, time_peresaryadky)
                        ready_vistrel_tank1 = False

                #   player2
                if event.key == pygame.K_UP:  # Обработка клавици "w"
                    dy_tank2 = -step
                    bullet_dy_tank2 = -step_bullet
                    bullet_dx_tank2 = 0
                    go_tank2 = True
                if event.key == pygame.K_DOWN:  # Обработка клавици "w"
                    dy_tank2 = step

                    bullet_dy_tank2 = step_bullet
                    bullet_dx_tank2 = 0
                    go_tank2 = True
                if event.key == pygame.K_LEFT:  # Обработка клавици "w"
                    dx_tank2 = -step
                    bullet_dx_tank2 = -step_bullet
                    bullet_dy_tank2 = 0
                    go_tank2 = True
                if event.key == pygame.K_RIGHT:  # Обработка клавици "w"
                    dx_tank2 = step
                    bullet_dx_tank2 = step_bullet
                    bullet_dy_tank2 = 0
                    go_tank2 = True
                if event.key == pygame.K_RETURN:
                    if ready_vistrel_tank2:
                        Bullet(tank2.x, tank2.y, bullet_dx_tank2, bullet_dy_tank2, 2)
                        pygame.mixer.music.load('data/zvuk_shoot (mp3cut.net).mp3')
                        pygame.mixer.music.play()
                        pygame.time.set_timer(EVENT_PERESAR_TANK2, time_peresaryadky)
                        ready_vistrel_tank2 = False
            if event.type == pygame.KEYUP:
                # player1
                if event.key == pygame.K_w:  # Обработка клавици "w"
                    dy_tank1 = 0
                    go_tank1 = False
                if event.key == pygame.K_s:  # Обработка клавици "w"
                    dy_tank1 = 0
                    go_tank1 = False
                if event.key == pygame.K_a:  # Обработка клавици "w"
                    dx_tank1 = 0
                    go_tank1 = False
                if event.key == pygame.K_d:  # Обработка клавици "w"
                    dx_tank1 = 0
                    go_tank1 = False
                #   player2
                if event.key == pygame.K_UP:  # Обработка клавици "w"
                    dy_tank2 = 0
                    go_tank2 = True
                if event.key == pygame.K_DOWN:  # Обработка клавици "w"
                    dy_tank2 = 0
                    go_tank2 = True
                if event.key == pygame.K_LEFT:  # Обработка клавици "w"
                    dx_tank2 = 0
                    go_tank2 = True
                if event.key == pygame.K_RIGHT:  # Обработка клавици "w"
                    dx_tank2 = 0
                    go_tank2 = True
            if event.type == EVENT_PERESAR_TANK1:
                ready_vistrel_tank1 = True
            if event.type == EVENT_PERESAR_TANK2:
                ready_vistrel_tank2 = True
        if go_tank1:
            tank1.move(tank1.x + dx_tank1, tank1.y + dy_tank1)
        if go_tank2:
            tank2.move(tank2.x + dx_tank2, tank2.y + dy_tank2)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update(event)
    podchet_scoreRed.render()
    podchet_scoreBlue.render()
    pygame.display.flip()
    clock.tick(fps)
