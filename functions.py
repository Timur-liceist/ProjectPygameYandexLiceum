import os
import sys

import pygame


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