import pygame, sys
import START_GUI
from pygame.locals import *

from Background import Background
from Player import Character
from Creep import Creep
from Button import Button

# from pygame import mixer
# mixer.music.load('Music_game.mp3')  # music
# mixer.music.play(-1)

window_width = 1100
window_height = 550
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Shooting Game Piu Piu')

# FPS
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

# size main character
crt_width = 100
crt_height = 100
player = pygame.image.load('main_1.png')

# size creep character
creep_width = 100
creep_height = 100
creep = pygame.image.load('creep_1.png')

# background
background = pygame.image.load('background.png').convert_alpha()
bg = Background(0, 0, window_width, window_height)

# size nhân vật xuất hiên
character = Character(0, int(window_height - crt_height), crt_width, crt_height, window_height)

# size creep xuất hiện
Creep = Creep(0, int(550 - creep_height), creep_width, creep_height)


def main():
    left_crt = False
    right_crt = False

    right_creep = False  # bot di chuyển tự động sang phải
    left_creep = True

    gravyti = 1
    score = 0

    # bullet
    bullet = 0

    while True:
        font = pygame.font.SysFont('time', 24)  # font chữ tính điểm
        font_bullet = pygame.font.SysFont('time', 40)

        show_score = font.render("Score : " + str(score), True, (255, 0, 0))
        show_bullet = font.render("Bullet : " + str(bullet), True, (255, 0, 0))
        show_no_bullet = font_bullet.render("No bullet- Press P to reload ", True, (51, 51, 0))

        def show():
            screen.blit(show_score, (999, 0))
            screen.blit(show_bullet, (0, 10))
            if bullet < 1:
                screen.blit(show_no_bullet, (390, 250))

        for event in pygame.event.get():  # các nút tương tác game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_a:
                    left_crt = True

                if event.key == K_d:
                    right_crt = True

                if character.flag_jump:
                    if event.key == K_w:
                        character.movement = 0
                        character.movement -= 20
                        character.flag_jump = False

                if event.key == K_SPACE:
                    bullet -= 1
                if event.key == K_p:
                    bullet += 1

            if event.type == KEYUP:
                if event.key == K_a:
                    left_crt = False
                if event.key == K_d:
                    right_crt = False

        character.movement += gravyti

        bg.draw()
        bg.move(character)
        character.draw(bg)
        character.move(left_crt, right_crt, character, bg)

        character.update()

        Creep.move(left_creep, right_creep, bg)
        Creep.draw(1100)

        show()

        if bullet < 0 or bullet >= 20:
            break

        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    main()
