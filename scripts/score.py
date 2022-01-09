import pygame
from scripts.variables import screen
class Score:

    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.score = 0
        self.color = color

    def render(self):
        font = pygame.font.Font(None, 50)
        text = font.render(f"{self.score}", True, self.color)
        text_x = self.x
        text_y = self.y
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, self.color, (text_x - 10, text_y - 10,
                                              text_w + 20, text_h + 20), 1)