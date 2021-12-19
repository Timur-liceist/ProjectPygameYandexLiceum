import pygame


class Player:
    pass


class Block:
    pass


class Board:
    # создание поля
    def init(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]

        for i in range(25):
            for j in range(25):
                if i == 0 or i == 24 or j == 0 or j == 24:
                    self.board[i][j] = 1
        for i in range(25):
            print(self.board[i])
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
                if self.board[h][w] == 1:
                    pygame.draw.rect(screen, "green", (x, y, self.cell_size, self.cell_size), 0)

                pygame.draw.rect(screen, "white", (x, y, self.cell_size, self.cell_size), 1)

    def get_cell(self, pos):
        column = (pos[0] - self.left) // self.cell_size
        row = (pos[1] - self.top) // self.cell_size
        if row < 0 or row > self.height:
            return None
        elif column < 0 or column > self.width:
            return None
        return row, column

    def on_click(self, cell_coords):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        print(cell)


pygame.display.set_caption('Танчики')
screen = pygame.display.set_mode((500, 500))
playground = Board(25, 25)
fps = 30  # количество кадров в секунду
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # player1
            if event.key == pygame.K_W: # Обработка клавици "w"
                pass
    screen.fill((0, 0, 0))
    playground.render(screen)
    pygame.display.flip()
    clock.tick(fps)