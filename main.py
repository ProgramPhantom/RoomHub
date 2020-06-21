import pygame
# import getAtmosData
import text as t

pygame.init()

WIDTH = 1500
HEIGHT = 900
winRect = pygame.Rect(0, 0, WIDTH, HEIGHT)
BGCOLOUR = (255, 255, 255)
DATA = {"temperature": 0}

texts = {}

win = pygame.display.set_mode((WIDTH, HEIGHT))

tempFont = pygame.font.Font('fonts/Arkitech Bold.ttf', 10)


def load():
    with open("text.txt", "r") as text:
        for l in text:
            dic = eval(l)
            texts["temperature"] = (t.Text(**dic))

    print(texts)


def draw():
    win.fill(BGCOLOUR)

    for t in texts.values():
        t.draw()

    pygame.display.update()


def update_stats():
    global DATA

    # DATA["temperature"] = getAtmosData.getTemps()


load()

r = True
while r:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False

    # update_stats()
    draw()
