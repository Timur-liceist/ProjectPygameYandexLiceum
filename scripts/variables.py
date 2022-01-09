import pygame
all_sprites = pygame.sprite.Group()
cell_size = 20
blocks_not_breaking = pygame.sprite.Group()
blocks_breaking = pygame.sprite.Group()
bullets_of_player1 = pygame.sprite.Group()
bullets_of_player2 = pygame.sprite.Group()
EVENT_PERESAR_TANK1 = 30
EVENT_PERESAR_TANK2 = 60
EVENT_SPAWN_TANK2 = 40
EVENT_SPAWN_TANK1 = 90
TIME = 150000
HP_TANKS = 3
HP_BASE = 5
GRAVITY = 0.1
screen_rect = (0, 0, 500, 500)
WIDTH, HEIGHT = SIZE_WINDOW = (650, 500)
screen = pygame.display.set_mode(SIZE_WINDOW)
time_spawn = 3500
TIMER_EVENT = 260
EVENT_SPAWN_BOX_WITH_HP = 80
time_spawn_of_box_with_hp = 6000