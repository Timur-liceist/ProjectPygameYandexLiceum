import pygame
from background import Background
from variables_for_menu import all_sprites, screen, color_before, color_after, WIDTH, HEIGHT
from button import Button
from main import start_game
import pygame_gui
from data.levels import level
fps = 60

running = True
background = Background()
# 250
# 320
# 390
button_for_start = Button("В бой!", 380, 390, 250, 60, color_before, "start", 40)
button_time_2 = Button("2 МИН", 380, 320, 60, 60, color_before, "min2", 20)
button_time_5 = Button("5 МИН", 475, 320, 60, 60, color_before, "min5", 20)
button_time_10 = Button("10 МИН", 570, 320, 60, 60, color_before, "min10", 20)
pygame.display.set_caption('Танчики')
clock = pygame.time.Clock()
manager =pygame_gui.UIManager((WIDTH, HEIGHT), "data/design_of_pygame_gui.json")
min_two_pressed = True
min_five_pressed = False
min_ten_pressed = False
level_for_start_game = "Три стены"
combobox = pygame_gui.elements.UIDropDownMenu(
    manager=manager,
    relative_rect=pygame.Rect((380, 250), (250, 60)),
    options_list=list(level.keys()),
    starting_option=list(level.keys())[0],
)

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
                    start_game(time_game, level_for_start_game)
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
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == combobox:
                    level_for_start_game = event.text
                    print(level)
        manager.process_events(event)

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    button_for_start.render(screen)
    button_time_2.render(screen)
    button_time_5.render(screen)
    button_time_10.render(screen)
    time_delta = clock.tick(fps) / 1000.0
    manager.draw_ui(screen)
    manager.update(time_delta)
    pygame.display.flip()
