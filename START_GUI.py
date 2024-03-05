import pygame, sys
from Button import Button
from Background import Background
import GameFPS
from Background import Background_start

pygame.init()

window_width = 1100
window_height = 550
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Shooting Game Piu Piu')

background = pygame.image.load('background.png').convert_alpha()
bg = Background(0, 0, window_width, window_height)

background_start = pygame.image.load('bg_start.png').convert_alpha()
bg_start = Background_start(0, 0, window_width, window_height)

bg_guide = pygame.image.load('bg_guide.png').convert_alpha()


def play():
    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()  # phát hiện bấm chuột
        GameFPS.main()

        PLAY_BACK = Button(image=None, pos=(0, 510),
                           text_input="BACK", font=pygame.font.SysFont('time', 24), base_color="red",
                           hovering_color="black")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        pygame.display.update()


def guide():
    while True:
        screen.blit(bg_guide, (205, 0))
        GUIDE_MOUSE_POS = pygame.mouse.get_pos()

        GUIDE_BACK = Button(image=None, pos=(1000, 500),
                            text_input="BACK", font=pygame.font.SysFont('time', 25), base_color="red",
                            hovering_color="yellow")

        GUIDE_BACK.changeColor(GUIDE_MOUSE_POS)
        GUIDE_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUIDE_BACK.checkForInput(GUIDE_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def back():
    while True:
        screen.blit(bg_guide, (205, 0))
        BACK_MOUSE_POS = pygame.mouse.get_pos()

        BACK = Button(image=None, pos=(1000, 500),
                      text_input="BACK", font=pygame.font.SysFont('time', 25), base_color="red",
                      hovering_color="yellow")

        BACK.changeColor(BACK_MOUSE_POS)
        BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(BACK_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        bg_start.draw_bg_start()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=None, pos=(550, 250),
                             text_input="PLAY", font=pygame.font.SysFont('time', 40), base_color="red",
                             hovering_color="yellow")

        GUIDE_BUTTON = Button(image=None, pos=(550, 300),
                              text_input="GUIDE", font=pygame.font.SysFont('time', 40), base_color="red",
                              hovering_color="yellow")

        for button in [PLAY_BUTTON, GUIDE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    guide()

                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()