import pygame

printTest = pygame.USEREVENT + 1

def test():
    print("Hello")


pygame.time.set_timer(printTest, 1000)

while True:
    for e in pygame.event.get():
        if e.type == printTest:
            test()
