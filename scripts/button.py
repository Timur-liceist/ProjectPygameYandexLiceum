import pygame
from scripts.variables_for_menu import all_sprites
pygame.init()
class Button(pygame.sprite.Sprite):
    def __init__(self, text, x, y, width, height, color, name_button, size_text):
        super().__init__(all_sprites)
        self.text = text
        self.size_text = size_text
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.name_button = name_button
    def set_color(self, color):
        self.color = color
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(screen, (240,150,0), (self.x, self.y, self.width, self.height), 5)
        font = pygame.font.Font(None, self.size_text)
        text = font.render(self.text, True, "black")
        text_w = text.get_width()
        text_h = text.get_height()
        text_x = self.x + self.width // 2 - text_w // 2
        text_y = self.y + self.height // 2 - text_h // 2
        screen.blit(text, (text_x, text_y))
    def mouse_on_button(self, coords):
        x, y = coords
        if x < self.x + self.width and x > self.x and y < self.y + self.height and y > self.y:
            return True