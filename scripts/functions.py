import os
import sys
import pygame
import sqlite3

def load_level(name):
    con = sqlite3.connect("../data/levels.db")
    cur = con.cursor()
    result = cur.execute(f"""SELECT level FROM levels
                WHERE name = '{name}'""").fetchall()[0][0].split("\n")
    result = list(map(lambda x: list(map(int, x.split())), result))
    con.close()
    return result
def load_image(name, w=None, h=None, colorkey=None):
    fullname = os.path.join(r'C:\Users\timka\PycharmProjects\ProjectPygameYandexLiceum\data', name)
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