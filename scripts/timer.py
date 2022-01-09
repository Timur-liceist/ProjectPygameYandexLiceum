import pygame
from scripts.variables import screen
class Timer:
    def __init__(self, x, y, TIME):
        self.x, self.y = x, y
        self.time = TIME

    def render(self):
        font = pygame.font.Font(None, 50)
        sec = self.time // 1000
        min = sec // 60
        sec = sec % 60
        if len(str(sec)) == 1:
            sec = f"0{sec}"
        text = font.render(f"{min}:{sec}", True, "green")
        text_x = self.x
        text_y = self.y
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, "green", (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)

    def update_timer(self):
        self.time -= 1000