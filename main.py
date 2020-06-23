import pygame
from pygame import Color
import getAtmosData
import text as t
import time

pygame.init()

WIDTH = 1500
HEIGHT = 900
winRect = pygame.Rect(0, 0, WIDTH, HEIGHT)
BGCOLOUR = (255, 255, 255)
DATA = {"temperature": "--", "humidity": "--"}
POLLTIME = 2000

# Fonts

henry = pygame.font.Font('fonts/Neufreit-ExtraBold.otf', 30)

# UI elements

# BACKGROUND
backgroundPic = pygame.image.load("img/Sunset.jpg")


# EVENTS

updateDataEvent = pygame.USEREVENT + 1

tick = pygame.time.Clock()

texts = {}

win = pygame.display.set_mode((WIDTH, HEIGHT))

tempFont = pygame.font.Font('fonts/Arkitech Bold.ttf', 10)


def load():
    with open("text.txt", "r") as text:
        for l in text:
            dic = eval(l)
            texts[dic["name"]] = t.Text(**dic)

    print(texts)


def draw():
    win.fill(BGCOLOUR)
    win.blit(backgroundPic, (0, 0))

    for t in texts.values():
        t.draw()

    pygame.display.update()


def update_stats():
    global DATA

    DATA["temperature"] = getAtmosData.getTemps()["temperature"]
    texts["temperature"].update_text(str(DATA["temperature"]) + "°C")

    DATA["humidity"] = getAtmosData.getTemps()["humidity"]  # This is cringe.
    texts["humidData"].update_text(str(DATA["humidity"]) + "°C")


# Timers
pygame.time.set_timer(updateDataEvent, POLLTIME)

load()

# SCHEDULED TASKS
pygame.time.set_timer(updateDataEvent, 2000)

r = True
while r:
    tick.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
        elif event.type == updateDataEvent:
            print("Updating Atmos Data!")
            update_stats()

    draw()
