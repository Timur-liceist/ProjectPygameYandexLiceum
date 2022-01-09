def start_game(TIME, level):
    import pygame
    from scripts.button import Button
    import sys
    from scripts.bullet import Bullet
    from scripts.functions import load_image
    from scripts.variables import all_sprites, cell_size, blocks_breaking, blocks_not_breaking, bullets_of_player1, \
        bullets_of_player2, EVENT_PERESAR_TANK1, EVENT_SPAWN_TANK2, EVENT_PERESAR_TANK2, EVENT_SPAWN_TANK1, TIMER_EVENT, \
        HP_TANKS, HP_BASE, screen, time_spawn, time_spawn_of_box_with_hp, EVENT_SPAWN_BOX_WITH_HP
    from scripts.bullet import AnimatedSprite
    from scripts.timer import Timer
    from scripts.hp import Hp
    from scripts.variables_for_menu import color_before, color_after
    from scripts.tank import Tank
    from scripts.text_win import TextWin
    from scripts.particles import create_particles
    from scripts.score import Score
    from scripts.board import Board
    from scripts.base import Base
    from scripts.new_hp import BoxWithHp

    podchet_scoreBlue = Score(515, 15, "blue")

    podchet_scoreRed = Score(570, 15, "red")


    def terminate():
        pygame.quit()
        sys.exit()


    pygame.display.set_caption('Танчики')

    playground = Board(25, 25, level_for_game=level)
    base1 = Base(12 * cell_size, 1 * cell_size, 1)
    base2 = Base(12 * cell_size, (25 - 2) * cell_size, 2)
    time_peresaryadky = 800
    pygame.time.set_timer(EVENT_PERESAR_TANK1, time_peresaryadky)
    pygame.time.set_timer(EVENT_PERESAR_TANK2, time_peresaryadky)
    timer = Timer(515, 100, TIME)

    base1_hp = Hp(500 // 2 - (HP_BASE * 15) // 2, -5, 1, HP_BASE)
    base2_hp = Hp(500 // 2 - (HP_BASE * 15) // 2, 500 - 25, 2, HP_BASE)
    pygame.time.set_timer(TIMER_EVENT, 1000)
    for i in range(playground.height):
        for j in range(playground.width):
            if playground.board[i][j] == 4:
                tank2 = Tank(j * cell_size, i * cell_size, 1)
                row_spawn_tank2, column_spawn_tank2 = j, i
            if playground.board[i][j] == 3:
                tank1 = Tank(j * cell_size, i * cell_size, 0)
                row_spawn_tank1, column_spawn_tank1 = j, i
    tank1.image = pygame.transform.rotate(tank1.image_of_tank, 180)

    pygame.init()
    start_timer_tank1 = False
    start_timer_tank2 = False
    FPS = 60  # количество кадров в секунду
    clock = pygame.time.Clock()
    running = True
    go_tank1 = False
    dx_tank1 = 0
    dy_tank1 = 0
    go_tank2 = False
    dx_tank2 = 0
    dy_tank2 = 0
    step = 1
    step_bullet = 3
    bullet_dx_tank1 = 0
    bullet_dy_tank1 = step_bullet
    bullet_dx_tank2 = 0
    time_peresaryadky = 800
    ready_vistrel_tank1 = True
    ready_vistrel_tank2 = True
    play = True
    bullet_dy_tank2 = -step_bullet
    hp_tank2 = Hp(545, 250, 2, HP_TANKS)
    hp_tank1 = Hp(545, 200, 1, HP_TANKS)
    # playing_music_of_tank_unichtozhen = True
    Tank(515, 200, 0)
    Tank(515, 250, 1)
    box_with_hp = BoxWithHp(playground)
    pygame.time.set_timer(EVENT_SPAWN_BOX_WITH_HP, time_spawn_of_box_with_hp)
    def update():
        for i in bullets_of_player1:
            if pygame.sprite.collide_mask(i, tank1) and i.player == 2:
                tank1.hp -= 1
                hp_tank1.update_hp()
                i.kill()
                if tank1.hp == 0:
                    podchet_scoreRed.score += 1
                if tank1.hp > 0:
                    pygame.mixer.music.load('../data/probitie.mp3')
                    pygame.mixer.music.play()
                AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                return
            elif pygame.sprite.collide_mask(i, tank2) and i.player == 1:
                tank2.hp -= 1
                i.kill()
                hp_tank2.update_hp()
                if tank2.hp > 0:
                    pygame.mixer.music.load('../data/probitie.mp3')
                    pygame.mixer.music.play()
                if tank2.hp == 0:
                    podchet_scoreBlue.score += 1
                AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                return
            if i.player == 1:
                for j in bullets_of_player2:
                    if pygame.sprite.collide_mask(i, j):
                        i.kill()
                        j.kill()
                        AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                        return
            elif i.player == 2:
                for j in bullets_of_player1:
                    if pygame.sprite.collide_mask(i, j):
                        i.kill()
                        AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                        j.kill()
                        return
            for j in blocks_not_breaking:
                if pygame.sprite.collide_mask(i, j):
                    i.kill()
                    AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                    return
            for j in blocks_breaking:
                if pygame.sprite.collide_mask(i, j):
                    i.kill()
                    AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                    j.kill()
                    return
            if pygame.sprite.collide_mask(i, base1):
                base1.hp -= 1
                AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                i.kill()
                base1_hp.update_hp()
            if pygame.sprite.collide_mask(i, base2):
                base2.hp -= 1
                base2_hp.update_hp()
                AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                i.kill()
        for i in bullets_of_player2:
            if pygame.sprite.collide_mask(i, tank1) and i.player == 2:
                tank1.hp -= 1
                hp_tank1.update_hp()
                i.kill()
                if tank1.hp == 0:
                    podchet_scoreRed.score += 1
                if tank1.hp > 0:
                    pygame.mixer.music.load('../data/probitie.mp3')
                    pygame.mixer.music.play()
                AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                return
            elif pygame.sprite.collide_mask(i, tank2) and i.player == 1:
                tank2.hp -= 1
                i.kill()
                hp_tank2.update_hp()
                if tank2.hp > 0:
                    pygame.mixer.music.load('../data/probitie.mp3')
                    pygame.mixer.music.play()
                if tank2.hp == 0:
                    podchet_scoreBlue.score += 1
                AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                return
            if i.player == 1:
                for j in bullets_of_player2:
                    if pygame.sprite.collide_mask(i, j):
                        i.kill()
                        j.kill()
                        AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                        return
            elif i.player == 2:
                for j in bullets_of_player1:
                    if pygame.sprite.collide_mask(i, j):
                        i.kill()
                        AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                        j.kill()
                        return
            for j in blocks_not_breaking:
                if pygame.sprite.collide_mask(i, j):
                    i.kill()
                    AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                    return
            for j in blocks_breaking:
                if pygame.sprite.collide_mask(i, j):
                    i.kill()
                    AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                    j.kill()
                    return
            if pygame.sprite.collide_mask(i, base1):
                base1.hp -= 1
                AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                i.kill()
                base1_hp.update_hp()
            if pygame.sprite.collide_mask(i, base2):
                base2.hp -= 1
                base2_hp.update_hp()
                AnimatedSprite(load_image("boom.png", cell_size * 5, 2 * cell_size), 5, 2, i.rect.x, i.rect.y)
                i.kill()
    flag_box_with_hp = True
    while running:
        print(tank1.hp, tank2.hp)
        if (podchet_scoreBlue.score == 5 or podchet_scoreRed.score == 5 or base1.hp == 0 or base2.hp == 0) and play:
            # if playing_music_of_tank_unichtozhen:
            #     playing_music_of_tank_unichtozhen = False
            create_particles((100, 100))
            create_particles((400, 100))
            create_particles((400, 400))
            create_particles((100, 400))
            create_particles((225, 250))
            create_particles((250, 250))
            button_to_menu = Button("Меню", 210, 350, 100, 50, color_before, "to_menu", 40)
            if base1.hp == 0:
                TextWin(500 // 2 - 200, 500 // 2 - 100, 1)
            else:
                TextWin(500 // 2 - 200, 500 // 2 - 100, 2)
            play = False
        elif timer.time == 0 and play:
            # if playing_music_of_tank_unichtozhen:
            #     playing_music_of_tank_unichtozhen = False
            create_particles((100, 100))
            create_particles((400, 100))
            create_particles((400, 400))
            create_particles((100, 400))
            create_particles((225, 250))
            create_particles((250, 250))
            button_to_menu = Button("Меню", 210, 350, 100, 50, color_before, "to_menu", 40)
            if podchet_scoreBlue.score < podchet_scoreRed.score:
                TextWin(500 // 2 - 200, 500 // 2 - 100, 1)
            elif podchet_scoreBlue.score == podchet_scoreRed.score:
                TextWin(500 // 2 - 200, 500 // 2 - 100, 3)
            else:
                TextWin(500 // 2 - 200, 500 // 2 - 100, 2)
            play = False
        if tank1.hp <= 0 and start_timer_tank1 is False:
            pygame.time.set_timer(EVENT_SPAWN_TANK1, time_spawn)
            start_timer_tank1 = True
        if tank2.hp <= 0 and start_timer_tank2 is False:
            pygame.time.set_timer(EVENT_SPAWN_TANK2, time_spawn)
            start_timer_tank2 = True
        if play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # player1
                    if event.key == pygame.K_w:  # Обработка клавици "w"
                        dy_tank1 = -step
                        bullet_dy_tank1 = -step_bullet
                        bullet_dx_tank1 = 0
                        go_tank1 = True
                    if event.key == pygame.K_s:  # Обработка клавици "w"
                        dy_tank1 = step
                        bullet_dy_tank1 = step_bullet
                        bullet_dx_tank1 = 0
                        go_tank1 = True
                    if event.key == pygame.K_a:  # Обработка клавици "w"
                        dx_tank1 = -step
                        bullet_dx_tank1 = -step_bullet
                        bullet_dy_tank1 = 0
                        go_tank1 = True
                    if event.key == pygame.K_d:  # Обработка клавици "w"
                        dx_tank1 = step
                        bullet_dx_tank1 = step_bullet
                        bullet_dy_tank1 = 0
                        go_tank1 = True
                    if event.key == pygame.K_SPACE:
                        if ready_vistrel_tank1 and tank1.hp > 0:
                            Bullet(tank1.x, tank1.y, bullet_dx_tank1, bullet_dy_tank1, 1)
                            pygame.mixer.music.load('../data/zvuk_shoot (mp3cut.net).mp3')
                            pygame.mixer.music.play()
                            pygame.time.set_timer(EVENT_PERESAR_TANK1, time_peresaryadky)
                            ready_vistrel_tank1 = False

                    #   player2
                    if event.key == pygame.K_UP:  # Обработка клавици "w"
                        dy_tank2 = -step
                        bullet_dy_tank2 = -step_bullet
                        bullet_dx_tank2 = 0
                        go_tank2 = True
                    if event.key == pygame.K_DOWN:  # Обработка клавици "w"
                        dy_tank2 = step

                        bullet_dy_tank2 = step_bullet
                        bullet_dx_tank2 = 0
                        go_tank2 = True
                    if event.key == pygame.K_LEFT:  # Обработка клавици "w"
                        dx_tank2 = -step
                        bullet_dx_tank2 = -step_bullet
                        bullet_dy_tank2 = 0
                        go_tank2 = True
                    if event.key == pygame.K_RIGHT:  # Обработка клавици "w"
                        dx_tank2 = step
                        bullet_dx_tank2 = step_bullet
                        bullet_dy_tank2 = 0
                        go_tank2 = True
                    if event.key == pygame.K_RETURN:
                        if ready_vistrel_tank2 and tank2.hp > 0:
                            Bullet(tank2.x, tank2.y, bullet_dx_tank2, bullet_dy_tank2, 2)
                            pygame.mixer.music.load('../data/zvuk_shoot (mp3cut.net).mp3')
                            pygame.mixer.music.play()
                            pygame.time.set_timer(EVENT_PERESAR_TANK2, time_peresaryadky)
                            ready_vistrel_tank2 = False
                if event.type == pygame.KEYUP:
                    # player1
                    if event.key == pygame.K_w:  # Обработка клавици "w"
                        dy_tank1 = 0
                        go_tank1 = False
                    if event.key == pygame.K_s:  # Обработка клавици "w"
                        dy_tank1 = 0
                        go_tank1 = False
                    if event.key == pygame.K_a:  # Обработка клавици "w"
                        dx_tank1 = 0
                        go_tank1 = False
                    if event.key == pygame.K_d:  # Обработка клавици "w"
                        dx_tank1 = 0
                        go_tank1 = False
                    #   player2
                    if event.key == pygame.K_UP:  # Обработка клавици "w"
                        dy_tank2 = 0
                        go_tank2 = True
                    if event.key == pygame.K_DOWN:  # Обработка клавици "w"
                        dy_tank2 = 0
                        go_tank2 = True
                    if event.key == pygame.K_LEFT:  # Обработка клавици "w"
                        dx_tank2 = 0
                        go_tank2 = True
                    if event.key == pygame.K_RIGHT:  # Обработка клавици "w"
                        dx_tank2 = 0
                        go_tank2 = True
                if event.type == EVENT_PERESAR_TANK1:
                    ready_vistrel_tank1 = True
                if event.type == EVENT_PERESAR_TANK2:
                    ready_vistrel_tank2 = True
                if event.type == EVENT_SPAWN_BOX_WITH_HP and not flag_box_with_hp:
                    box_with_hp = BoxWithHp(playground)
                    flag_box_with_hp = True
                if event.type == EVENT_SPAWN_TANK1 and tank1.hp <= 0:
                    hp_tank1 = Hp(545, 200, 1, HP_TANKS)
                    tank1.kill()
                    hp_tank1.hp = HP_TANKS

                    # tank1 = Tank(column_spawn_tank1 * cell_size, row_spawn_tank1 * cell_size, 1)
                    tank1 = Tank(row_spawn_tank1 * cell_size, column_spawn_tank1 * cell_size, 0)
                    start_timer_tank1 = False
                if event.type == EVENT_SPAWN_TANK2 and tank2.hp <= 0:

                    hp_tank2 = Hp(545, 250, 2, HP_TANKS)
                    hp_tank2.hp = HP_TANKS
                    tank2.kill()
                    # tank2 = Tank(column_spawn_tank2 * cell_size, row_spawn_tank2 * cell_size, 2)
                    tank2 = Tank(row_spawn_tank2 * cell_size, column_spawn_tank2 * cell_size, 1)
                    start_timer_tank1 = False
                if event.type == TIMER_EVENT:
                    timer.update_timer()
            if go_tank1:
                tank1.move(tank1.x + dx_tank1, tank1.y + dy_tank1)
            if go_tank2:
                tank2.move(tank2.x + dx_tank2, tank2.y + dy_tank2)
        else:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    if button_to_menu.mouse_on_button(event.pos):
                        button_to_menu.set_color(color_after)
                    if not button_to_menu.mouse_on_button(event.pos):
                        button_to_menu.set_color(color_before)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button_to_menu.mouse_on_button(event.pos):
                            running = False
                            for i in all_sprites:
                                i.kill()
                if event.type == pygame.QUIT:
                    sys.exit()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        try:
            all_sprites.update(event)
        except Exception:
            pass
        podchet_scoreRed.render()
        podchet_scoreBlue.render()
        timer.render()
        try:
            button_to_menu.render(screen)
        except Exception:
            pass
        if pygame.sprite.collide_mask(tank1, box_with_hp):
            flag_box_with_hp = False
            box_with_hp.kill()
            box_with_hp.rect.x = -100
            for i in hp_tank1.hearts:
                i.kill()
            hp_tank1 = Hp(545, 200, 1, HP_TANKS)
            tank1.hp = HP_TANKS
        if pygame.sprite.collide_mask(tank2, box_with_hp):
            flag_box_with_hp = False
            box_with_hp.kill()
            box_with_hp.rect.x = -100
            for i in hp_tank2.hearts:
                i.kill()
            hp_tank2 = Hp(545, 250, 2, HP_TANKS)
            tank2.hp = HP_TANKS
        update()
        pygame.display.flip()
        clock.tick(FPS)
