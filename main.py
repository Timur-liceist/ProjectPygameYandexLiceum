import pygame
import os
import sys

all_sprites = pygame.sprite.Group()


def load_image(name, w, h, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
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
    image_of_NotBreak = load_image("ntbreak_blok.png", 20, 20)

    def __init__(self, coords, type):
        super().__init__(all_sprites)
        self.t = ["break", "NotBreak"]
        self.type = type

        self.x, self.y = coords
        if self.t[self.type] == "NotBreak":
            self.image = Block.image_of_NotBreak
        else:
            pass
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
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

    def update(self):
        pass


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]

        for i in range(25):
            for j in range(25):
                if i == 0 or i == 24 or j == 0 or j == 24:
                    self.board[i][j] = 1
        # for i in range(25):
        # print(self.board[i])
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 20

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for w in range(self.width):
            for h in range(self.height):
                x = self.left + w * self.cell_size
                y = self.top + h * self.cell_size
                if self.board[h][w] == 0:
                    Grass(w * 20, h * 20)
                if self.board[h][w] == 1:
                    Block((w * 20, h * 20), 1)

                pygame.draw.rect(screen, "white", (x, y, self.cell_size, self.cell_size), 1)


pygame.display.set_caption('Танчики')
screen = pygame.display.set_mode((500, 500))
playground = Board(25, 25)

fps = 30 # количество кадров в секунду
clock = pygame.time.Clock()
# for i in range(25):
# for j in range(25):
# Grass(i * 20, j * 20)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # player1
            if event.key == pygame.K_w: # Обработка клавици "w"
                pass

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    playground.render(screen)
    pygame.display.flip()
    clock.tick(fps)