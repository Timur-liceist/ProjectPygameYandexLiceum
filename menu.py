import pygame
from background import Background
from variables_for_menu import all_sprites, screen, color_before, color_after
from button import Button
from main import start_game
fps = 60
running = True
background = Background()
button_for_start = Button("В бой!", 450, 200, 250, 60, color_before, "start", 40)
button_time_2 = Button("2 МИН", 450, 270, 60, 60, color_before, "min2", 20)
button_time_5 = Button("5 МИН", 545, 270, 60, 60, color_before, "min5", 20)
button_time_10 = Button("10 МИН", 640, 270, 60, 60, color_before, "min10", 20)
pygame.display.set_caption('Танчики')
clock = pygame.time.Clock()
min_two_pressed = True
min_five_pressed = False
min_ten_pressed = False
button_time_2.set_color(color_after)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button_for_start.mouse_on_button(event.pos):
                    if min_two_pressed:
                        time_game = 2 * 60 * 1000
                    if min_five_pressed:
                        time_game = 5 * 60 * 1000
                    if min_ten_pressed:
                        time_game = 10 * 60 * 1000
                    start_game(time_game, 0)
                if button_time_10.mouse_on_button(event.pos):
                    print(1)
                    min_two_pressed = False
                    min_five_pressed = False
                    min_ten_pressed = True
                if button_time_5.mouse_on_button(event.pos):
                    min_two_pressed = False
                    min_five_pressed = True
                    min_ten_pressed = False
                if button_time_2.mouse_on_button(event.pos):
                    min_two_pressed = True
                    min_five_pressed = False
                    min_ten_pressed = False
        if event.type == pygame.MOUSEMOTION:
            if button_for_start.mouse_on_button(event.pos):
                button_for_start.set_color(color_after)
            if button_time_2.mouse_on_button(event.pos):
                button_time_2.set_color(color_after)
            if button_time_5.mouse_on_button(event.pos):
                button_time_5.set_color(color_after)
            if button_time_10.mouse_on_button(event.pos):
                button_time_10.set_color(color_after)
            if not button_time_10.mouse_on_button(event.pos) and not min_ten_pressed:
                button_time_10.set_color(color_before)
            if not button_time_5.mouse_on_button(event.pos) and not min_five_pressed:
                button_time_5.set_color(color_before)
            if not button_time_2.mouse_on_button(event.pos) and not min_two_pressed:
                button_time_2.set_color(color_before)
            if not button_for_start.mouse_on_button(event.pos):
                button_for_start.set_color(color_before)

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    button_for_start.render(screen)
    button_time_2.render(screen)
    button_time_5.render(screen)
    button_time_10.render(screen)

    pygame.display.flip()
    clock.tick(fps)
