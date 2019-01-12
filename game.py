#msk9pe
#chj5vg

# IMPORTANT *Graders please read*
# On some computers, specifically Macs from what we've seen, the game does not run as intended.
# The gameboxes move much slower on Macs, despite running the same code smoothly on PCs
# causing the game to move too slowly
# We have consulted TAs about this problem and they told us it has nothing to do with our code
# but instead it may be a problem with gamebox itself or due to differences in computer operating systems.

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
level1_platforms = [
    gamebox.from_color(200, 400, 'yellow2', 1200, 50),
    gamebox.from_color(200, 200, 'yellow2', 1200, 50),
    gamebox.from_color(875, 440, 'yellow2', 150, 30),
    gamebox.from_color(875, 240, 'yellow2', 150, 30),
    gamebox.from_color(1025, 470, 'yellow2', 150, 30),
    gamebox.from_color(1025, 270, 'yellow2', 150, 30),
    gamebox.from_color(1175, 500, 'yellow2', 150, 30),
    gamebox.from_color(1175, 300, 'yellow2', 150, 30),
    gamebox.from_color(1325, 530, 'yellow2', 150, 30),
    gamebox.from_color(1325, 330, 'yellow2', 150, 30),
    gamebox.from_color(1525, 500, 'yellow2', 150, 30),
    gamebox.from_color(1525, 300, 'yellow2', 150, 30),
    gamebox.from_color(1675, 470, 'yellow2', 150, 30),
    gamebox.from_color(1675, 270, 'yellow2', 150, 30),
    gamebox.from_color(1825, 440, 'yellow2', 150, 30),
    gamebox.from_color(1825, 240, 'yellow2', 150, 30),
    gamebox.from_color(2000, 200, 'yellow2', 30, 500),
    gamebox.from_color(2000, 550, 'yellow2', 150, 30),
    gamebox.from_color(2510, 375, 'yellow2', 30, 500),
    gamebox.from_color(2510, 50, 'yellow2', 150, 30),
    gamebox.from_color(3020, 200, 'yellow2', 30, 500),
    gamebox.from_color(3020, 550, 'yellow2', 150, 30),
    gamebox.from_color(3250, 250, 'yellow2', 150, 30),
    gamebox.from_color(3400, 220, 'yellow2', 150, 30),
    gamebox.from_color(3400, 450, 'yellow2', 150, 30),
    gamebox.from_color(3550, 190, 'yellow2', 150, 30),
    gamebox.from_color(3550, 480, 'yellow2', 150, 30),
    gamebox.from_color(3650, 320, 'yellow2', 150, 30),
    gamebox.from_color(3700, 450, 'yellow2', 150, 30),
    gamebox.from_color(3700, 220, 'yellow2', 150, 30),
    gamebox.from_color(3850, 420, 'yellow2', 150, 30),
    gamebox.from_color(3850, 250, 'yellow2', 150, 30),
    gamebox.from_color(4000, 390, 'yellow2', 150, 30),
    gamebox.from_color(4000, 280, 'yellow2', 150, 30),
    gamebox.from_color(4310, 300, 'yellow2', 30, 390),
    gamebox.from_color(4310, 50, 'yellow2', 150, 30),
    gamebox.from_color(4310, 550, 'yellow2', 150, 30),
    gamebox.from_color(4550, 300, 'yellow2', 150, 30),
    gamebox.from_color(4700, 200, 'yellow2', 150, 30),
    gamebox.from_color(4850, 300, 'yellow2', 150, 30),
    gamebox.from_color(5000, 200, 'yellow2', 150, 30),
    gamebox.from_color(5150, 300, 'yellow2', 150, 30),
    gamebox.from_color(5300, 200, 'yellow2', 150, 30),
    gamebox.from_color(5450, 300, 'yellow2', 150, 30),
    gamebox.from_color(5650, 50, 'yellow2', 150, 30),
    gamebox.from_color(5800, 150, 'yellow2', 150, 30),
    gamebox.from_color(5950, 50, 'yellow2', 150, 30),
    gamebox.from_color(6150, 300, 'yellow2', 150, 30),
    gamebox.from_color(6300, 330, 'yellow2', 150, 30),
    gamebox.from_color(6300, 200, 'yellow2', 150, 30),
    gamebox.from_color(6450, 300, 'yellow2', 150, 30),
    gamebox.from_color(6500, 250, 'green', 30, 80),
]
level2_platforms = [
    gamebox.from_color(200, 400, 'turquoise1', 1100, 50),
    gamebox.from_color(200, 200, 'turquoise1', 1100, 50),
    gamebox.from_color(900, 445, 'turquoise1', 200, 30),
    gamebox.from_color(1100, 500, 'turquoise1', 150, 30),
    gamebox.from_color(1270, 555, 'turquoise1', 170, 30),
    gamebox.from_color(1430, 350, 'turquoise1', 150, 30),
    gamebox.from_color(1670, 500, 'turquoise1', 170, 30),
    gamebox.from_color(1890, 350, 'turquoise1', 150, 30),
    gamebox.from_color(2060, 295, 'turquoise1', 150, 30),
    gamebox.from_color(2230, 240, 'turquoise1', 150, 30),
    gamebox.from_color(2500, 500, 'turquoise1', 150, 30),
    gamebox.from_color(2700, 230, 'turquoise1', 150, 30),
    gamebox.from_color(2950, 500, 'turquoise1', 150, 30),
    gamebox.from_color(3075, 470, 'turquoise1', 150, 30),
    gamebox.from_color(3075, 370, 'turquoise1', 150, 30),
    gamebox.from_color(3200, 500, 'turquoise1', 150, 30),
    gamebox.from_color(3400, 565, 'turquoise1', 150, 30),
    gamebox.from_color(3600, 430, 'turquoise1', 150, 30),
    gamebox.from_color(3800, 565, 'turquoise1', 150, 30),
    gamebox.from_color(4300, 50, 'turquoise1', 150, 30),
    gamebox.from_color(4800, 500, 'turquoise1', 150, 30),
    gamebox.from_color(4940, 420, 'turquoise1', 150, 30),
    gamebox.from_color(5040, 360, 'turquoise1', 150, 30),
    gamebox.from_color(5160, 280, 'turquoise1', 150, 30),
    gamebox.from_color(5400, 100, 'turquoise1', 150, 30),
    gamebox.from_color(5400, 460, 'turquoise1', 150, 30),
    gamebox.from_color(5610, 280, 'turquoise1', 150, 30),
    gamebox.from_color(5800, 100, 'turquoise1', 150, 30),
    gamebox.from_color(6100, 280, 'turquoise1', 150, 30),
    gamebox.from_color(6100, 400, 'turquoise1', 150, 30),
    gamebox.from_color(6150, 340, 'green', 50, 100),
]
level3_platforms = [
    gamebox.from_color(200, 401, 'darkorange', 1100, 50),
    gamebox.from_color(200, 200, 'darkorange', 1100, 50),
    gamebox.from_color(930, 500, 'darkorange', 150, 30),
    gamebox.from_color(970, 380, 'darkorange', 150, 30),
    gamebox.from_color(990, 470, 'darkorange', 30, 30),
    gamebox.from_color(1080, 500, 'darkorange', 150, 30),
    gamebox.from_color(1050, 470, 'darkorange', 30, 30),
    gamebox.from_color(1080, 380, 'darkorange', 150, 30),
    gamebox.from_color(1140, 410, 'darkorange', 30, 30),
    gamebox.from_color(1230, 500, 'darkorange', 150, 30),
    gamebox.from_color(1210, 470, 'darkorange', 30, 30),
    gamebox.from_color(1230, 380, 'darkorange', 150, 30),
    gamebox.from_color(1330, 470, 'darkorange', 30, 30),
    gamebox.from_color(1380, 500, 'darkorange', 170, 30),
    gamebox.from_color(1380, 380, 'darkorange', 150, 30),
    gamebox.from_color(1440, 410, 'darkorange', 30, 30),
    gamebox.from_color(1530, 500, 'darkorange', 150, 30),
    gamebox.from_color(1515, 470, 'darkorange', 30, 30),
    gamebox.from_color(1530, 380, 'darkorange', 150, 30),
    gamebox.from_color(1590, 410, 'darkorange', 30, 30),
    gamebox.from_color(1680, 500, 'darkorange', 150, 30),
    gamebox.from_color(1680, 380, 'darkorange', 150, 30),
    gamebox.from_color(1740, 470, 'darkorange', 30, 30),
    gamebox.from_color(1830, 380, 'darkorange', 150, 30),
    gamebox.from_color(1830, 550, 'darkorange', 150, 30),
    gamebox.from_color(1850, 520, 'darkorange', 30, 30),
    gamebox.from_color(1850, 410, 'darkorange', 30, 30),
    gamebox.from_color(1980, 410, 'darkorange', 150, 30),
    gamebox.from_color(1980, 520, 'darkorange', 150, 30),
    gamebox.from_color(2040, 490, 'darkorange', 30, 30),
    gamebox.from_color(2330, 150, 'darkorange', 150, 30),
    gamebox.from_color(2510, 50, 'darkorange', 150, 30),
    gamebox.from_color(2880, 400, 'darkorange', 150, 30),
    gamebox.from_color(3030, 475, 'darkorange', 150, 30),
    gamebox.from_color(3180, 550, 'darkorange', 150, 30),
    gamebox.from_color(3330, 400, 'darkorange', 150, 30),
    gamebox.from_color(3390, 430, 'darkorange', 30, 30),
    gamebox.from_color(3480, 570, 'darkorange', 150, 30),
    gamebox.from_color(3540, 540, 'darkorange', 30, 30),
    gamebox.from_color(3650, 350, 'darkorange', 150, 30),
    gamebox.from_color(3710, 380, 'darkorange', 30, 30),
    gamebox.from_color(3820, 570, 'darkorange', 150, 30),
    gamebox.from_color(3880, 540, 'darkorange', 30, 30),
    gamebox.from_color(4280, 70, 'darkorange', 150, 30),
    gamebox.from_color(4430, 400, 'darkorange', 150, 30),
    gamebox.from_color(4430, 100, 'darkorange', 150, 30),
    gamebox.from_color(4580, 130, 'darkorange', 150, 30),
    gamebox.from_color(4610, 340, 'darkorange', 30, 30),
    gamebox.from_color(4580, 370, 'darkorange', 150, 30),
    gamebox.from_color(4730, 160, 'darkorange', 150, 30),
    gamebox.from_color(4760, 190, 'darkorange', 30, 30),
    gamebox.from_color(4730, 340, 'darkorange', 150, 30),
    gamebox.from_color(4880, 190, 'darkorange', 150, 30),
    gamebox.from_color(4880, 310, 'darkorange', 150, 30),
    gamebox.from_color(4910, 280, 'darkorange', 30, 30),
    gamebox.from_color(4940, 198, 'darkorange', 150, 45),
    gamebox.from_color(5030, 290, 'darkorange', 150, 30),
    gamebox.from_color(5350, 50, 'darkorange', 150, 30),
    gamebox.from_color(5900, 560, 'darkorange', 150, 30),
    gamebox.from_color(6400, -150, 'darkorange', 100, 500),
    gamebox.from_color(6400, 450, 'darkorange', 100, 500),
    gamebox.from_color(6500, -100, 'darkorange', 100, 500),
    gamebox.from_color(6500, 500, 'darkorange', 100, 500),
    gamebox.from_color(6600, -50, 'darkorange', 100, 500),
    gamebox.from_color(6600, 550, 'darkorange', 100, 500),
    gamebox.from_color(6700, 0, 'darkorange', 100, 500),
    gamebox.from_color(6700, 600, 'darkorange', 100, 500),
    gamebox.from_color(6800, 50, 'darkorange', 100, 500),
    gamebox.from_color(6800, 650, 'darkorange', 100, 500),
    gamebox.from_color(6900, 100, 'darkorange', 100, 500),
    gamebox.from_color(6900, 700, 'darkorange', 100, 500),
    gamebox.from_color(7000, 150, 'darkorange', 100, 500),
    gamebox.from_color(7000, 750, 'darkorange', 100, 500),
    gamebox.from_color(7100, 200, 'darkorange', 100, 500),
    gamebox.from_color(7100, 800, 'darkorange', 100, 500),
    gamebox.from_color(7200, 250, 'darkorange', 100, 500),
    gamebox.from_color(7300, 200, 'darkorange', 100, 500),
    gamebox.from_color(7300, 800, 'darkorange', 100, 500),
    gamebox.from_color(7400, 150, 'darkorange', 100, 500),
    gamebox.from_color(7400, 750, 'darkorange', 100, 500),
    gamebox.from_color(7500, 100, 'darkorange', 100, 500),
    gamebox.from_color(7500, 700, 'darkorange', 100, 500),
    gamebox.from_color(7600, 50, 'darkorange', 100, 500),
    gamebox.from_color(7600, 650, 'darkorange', 100, 500),
    gamebox.from_color(7700, 0, 'darkorange', 100, 500),
    gamebox.from_color(7700, 600, 'darkorange', 100, 500),
    gamebox.from_color(8090, 570, 'darkorange', 150, 30),
    gamebox.from_color(8680, 30, 'darkorange', 150, 30),
    gamebox.from_color(8740, 70, 'green', 30, 100),
]

start_screen_background = gamebox.from_image(400, 375, "https://img00.deviantart.net/96b4/i/2012/115/8/c/mega_man_2_wallpaper_by_mlsterben-d4xl0fn.jpg")
start_screen_background.scale_by(.9)
extra_between_level_background = gamebox.from_color(400, 50, 'black', 800, 200)
level1_background = gamebox.from_image(400, 300, "https://tcrf.net/images/e/e9/MegaARCTreesBG1.png")
level1_background.scale_by(3.15)
level2_background = gamebox.from_image(400, 300, "https://tcrf.net/images/5/5a/RM7ShadeBG2Sample.png")
level2_background.scale_by(1.57)
level3_background = gamebox.from_image(400, 300, "i.imgur.com/Eck5M.png")
level3_background.scale_by(1.6)
character_sheet = gamebox.load_sprite_sheet(
    "http://hikari.zackthehuman.com/blog/images/graphics/rock-running-3.png", 1, 3)
character = gamebox.from_image(camera.x, camera.y, character_sheet[0])
character.scale_by(.3)
character.cool_down = 0
ticks = 0
life_time = 0
game_on = False
lose = False
down_gravity = True
level = 1
start_level2 = True
start_level3 = True
lives = 5
current_level = gamebox.from_text(400, 40, "Level " + str(level), 30, "purple")
lives_counter = gamebox.from_text(650, 40, "Lives: " + str(lives), 30, "purple")

rainbow_ticks = 0
def start_screen():
    global game_on
    global start_level2
    global start_level3
    global life_time
    global rainbow_ticks
    rainbow_ticks += 1
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    random.seed()
    random_number = random.randint(0, 5)
    if rainbow_ticks % 8 == 0:
        start_screen_title1 = gamebox.from_text(325, 200, 'MEGA', 100, colors[random_number])
        start_screen_title2 = gamebox.from_text(325, 260, 'GRAVITY', 100, colors[random_number])
        start_screen_title3 = gamebox.from_text(325, 320, 'MAN', 100, colors[random_number])
    else:
        start_screen_title1 = gamebox.from_text(325, 200, 'MEGA', 100, colors[random_number])
        start_screen_title2 = gamebox.from_text(325, 260, 'GRAVITY', 100, colors[random_number])
        start_screen_title3 = gamebox.from_text(325, 320, 'MAN', 100, colors[random_number])

    camera.draw(start_screen_background)
    if level == 1:
        start_screen_name1 = gamebox.from_text(50, 50, "Created by:", 20, 'tan')
        start_screen_name2 = gamebox.from_text(105, 65, "Matthew Kovalenko: msk9pe", 20, 'tan')
        start_screen_name3 = gamebox.from_text(94, 80, "Christian Jenkins: chj5vg", 20, 'tan')
        start_screen_instructions1 = gamebox.from_text(325, 400, "Instructions:", 30, 'tan')
        start_screen_instructions2 = gamebox.from_text(325, 420, "Press SPACE to flip gravity", 25, 'tan')
        start_screen_instructions3 = gamebox.from_text(325, 460, "Press SPACE to start the game!", 25, 'tan')

        camera.draw(start_screen_name1)
        camera.draw(start_screen_name2)
        camera.draw(start_screen_name3)
        camera.draw(start_screen_title1)
        camera.draw(start_screen_title2)
        camera.draw(start_screen_title3)
        camera.draw(start_screen_instructions1)
        camera.draw(start_screen_instructions2)
        camera.draw(start_screen_instructions3)
    elif level == 2:
        if start_level2:
            game_on = False
            life_time = 0
            start_level2 = False
        upper_between_level = gamebox.from_text(325, 250, 'Level ' + str(level - 1) + '  cleared', 30, 'whitesmoke')
        lower_between_level = gamebox.from_text(325, 300, 'Press SPACE to start level ' + str(level), 30, 'whitesmoke')
        camera.draw(upper_between_level)
        camera.draw(lower_between_level)
        camera.draw(extra_between_level_background)
    elif level == 3:
        if start_level3:
            game_on = False
            life_time = 0
            start_level3 = False
        upper_between_level = gamebox.from_text(325, 250, 'Level ' + str(level - 1) + '  cleared', 30, 'whitesmoke')
        lower_between_level = gamebox.from_text(325, 300, 'Press SPACE to start level ' + str(level), 30, 'whitesmoke')
        camera.draw(upper_between_level)
        camera.draw(lower_between_level)
        camera.draw(extra_between_level_background)


def use_platforms():
    global level
    character.move_speed()
    if level == 1:
        for platform in level1_platforms:
            character.move_to_stop_overlapping(platform)
    if level == 2:
        for platform in level2_platforms:
            character.move_to_stop_overlapping(platform)
    if level == 3:
        for platform in level3_platforms:
            character.move_to_stop_overlapping(platform)


def game_over():
    global life_time
    global lives
    global lives_counter
    lives -= 1
    if lives > 0:
        character.y = 300
        character.x = 400
        if level == 1:
            for platform in level1_platforms:
                platform.x -= platform.speedx * life_time
        elif level == 2:
            for platform in level2_platforms:
                platform.x -= platform.speedx * life_time
        elif level == 3:
            for platform in level3_platforms:
                platform.x -= platform.speedx * life_time
        lives_counter = gamebox.from_text(650, 40, "Lives: " + str(lives), 30, "purple")
    else:
        game_over = gamebox.from_text(400, 300, "Game Over", 60, "red")
        camera.draw(game_over)
        lives_counter = gamebox.from_text(650, 40, "Lives: 0", 30, "purple")
    life_time = 0


def win_game():
    global level
    global current_level
    if level == 1 or level == 2:
        level += 1
        current_level = gamebox.from_text(400, 40, "Level " + str(level), 30, "purple")
        start_screen()
    elif level == 3:
        camera.draw(start_screen_background)
        camera.draw(extra_between_level_background)
        win_game1 = gamebox.from_text(325, 200, "Congratulations!", 60, "green")
        win_game2 = gamebox.from_text(325, 250, "You've beat the game!", 60, "green")
        win_game3 = gamebox.from_text(325, 350, "Thanks for playing!", 60, "green")

        camera.draw(win_game1)
        camera.draw(win_game2)
        camera.draw(win_game3)
        gamebox.pause()



def tick(keys):
    global game_on
    global down_gravity
    global ticks
    global life_time
    start_screen()
    if pygame.K_SPACE in keys:
        game_on = True
    if game_on:
        ticks += 1
        life_time += 1
        character.image = character_sheet[(ticks // 3) % 3]
        if down_gravity:
            character.speedy = 6
            use_platforms()
        else:
            character.speedy = -6
            use_platforms()

        if level == 1:
            camera.draw(level1_background)
            for platform in level1_platforms:
                camera.draw(platform)
                platform.speedx = -6
                platform.move_speed()

                if character.bottom_touches(platform) or character.top_touches(platform):
                    if pygame.K_SPACE in keys:
                        down_gravity = not down_gravity
                        character.rotate(180)
                        character.flip()
                        keys.remove(pygame.K_SPACE)
                if character.top >= camera.bottom:
                    game_over()
                if character.bottom <= camera.top:
                    game_over()
                if character.right <= camera.left:
                    game_over()
                if character.right_touches(level1_platforms[-1]):
                    win_game()
        elif level == 2:
            camera.draw(level2_background)
            for platform in level2_platforms:
                camera.draw(platform)
                platform.speedx = -6
                platform.move_speed()

                if character.bottom_touches(platform) or character.top_touches(platform):
                    if pygame.K_SPACE in keys:
                        down_gravity = not down_gravity
                        character.rotate(180)
                        character.flip()
                        keys.remove(pygame.K_SPACE)
                if character.top >= camera.bottom:
                    game_over()
                if character.bottom <= camera.top:
                    game_over()
                if character.right <= camera.left:
                    game_over()
                if character.right_touches(level2_platforms[-1]):
                    win_game()
        elif level == 3:
            camera.draw(level3_background)
            for platform in level3_platforms:
                camera.draw(platform)
                platform.speedx = -6
                platform.move_speed()

                if character.bottom_touches(platform) or character.top_touches(platform):
                    if pygame.K_SPACE in keys:
                        down_gravity = not down_gravity
                        character.rotate(180)
                        character.flip()
                        keys.remove(pygame.K_SPACE)
                if character.top >= camera.bottom:
                    game_over()
                if character.bottom <= camera.top:
                    game_over()
                if character.right <= camera.left:
                    game_over()
                if character.right_touches(level3_platforms[-1]):
                    win_game()

        camera.draw(character)
        camera.draw(current_level)
        camera.draw(lives_counter)
    camera.display()
gamebox.timer_loop(60, tick)
