import pygame
import os
import sys
from data.level import level

all_sprites = pygame.sprite.Group()
cell_size = 20
blocks_not_breaking = pygame.sprite.Group()
bullets_of_player1 = pygame.sprite.Group()
bullets_of_player2 = pygame.sprite.Group()


def load_image(name, w, h, colorkey=None):
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
    image = pygame.transform.scale(image, (w, h))
    return image


def terminate():
    pygame.quit()
    sys.exit()


class Block(pygame.sprite.Sprite):
    image_of_NotBreak = load_image("ntbreak_blokVersion2.png", cell_size, cell_size)

    def __init__(self, coords, type):
        super().__init__(all_sprites)
        self.t = ["break", "NotBreak"]
        self.type = type

        self.x, self.y = coords
        if self.t[self.type] == "NotBreak":
            blocks_not_breaking.add(self)
            self.image = Block.image_of_NotBreak
        else:
            pass
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, *args):
        pass


class Grass(pygame.sprite.Sprite):
    image_of_grass = load_image("grass.jpg", 25, 25)

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
                if self.board[h][w] == 0:
                    Grass(w * cell_size, h * cell_size)
                if self.board[h][w] == 1:
                    Block((w * cell_size, h * cell_size), 1)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        # for w in range(self.width):
        #     for h in range(self.height):
        #         x = self.left + w * self.cell_size
        #         y = self.top + h * self.cell_size
        #         if self.board[h][w] == 0:
        #             Grass(w * cell_size, h * cell_size)
        #         if self.board[h][w] == 1:
        #             Block((w * cell_size, h * cell_size), 1)
        pass


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
        elif pygame.sprite.collide_mask(self, tank2) and self.player == 1:
            tank2.hp -= 1
            self.kill()
        if self.player == 1:
            for i in bullets_of_player2:
                if pygame.sprite.collide_mask(self, i):
                    self.kill()
                    i.kill()
                    break
        elif self.player == 2:
            for i in bullets_of_player1:
                if pygame.sprite.collide_mask(self, i):
                    self.kill()
                    i.kill()
                    break
        for i in blocks_not_breaking:
            if pygame.sprite.collide_mask(self, i):
                self.kill()


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
        if x < self.x:
            self.image = pygame.transform.rotate(self.image_of_tank, 90)
        if y > self.y:
            self.image = pygame.transform.rotate(self.image_of_tank, 180)
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

    def update(self, *args):
        if self.hp == 0:
            terminate()


pygame.display.set_caption('Танчики')
screen = pygame.display.set_mode((500, 500))
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
tank1 = Tank(12 * cell_size, 4 * cell_size, 0)
step = 1.5
step_bullet = 3
tank2 = Tank(12 * cell_size, (25 - 4) * cell_size, 1)
tank1.image = pygame.transform.rotate(tank1.image_of_tank, 180)
bullet_dx_tank1 = 0
bullet_dy_tank1 = step
bullet_dx_tank2 = 0
bullet_dy_tank2 = -step
while running:
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
                Bullet(tank1.x, tank1.y, bullet_dx_tank1, bullet_dy_tank1, 1)

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
                Bullet(tank2.x, tank2.y, bullet_dx_tank2, bullet_dy_tank2, 2)
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
    if go_tank1:
        tank1.move(tank1.x + dx_tank1, tank1.y + dy_tank1)
    if go_tank2:
        tank2.move(tank2.x + dx_tank2, tank2.y + dy_tank2)
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update(event)
    pygame.display.flip()
    clock.tick(fps)



