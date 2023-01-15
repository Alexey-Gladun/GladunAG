import pygame as pg

pg.init()
RES = width, height = 1200, 800
screen = pg.display.set_mode(RES)
clock = pg.time.Clock()
FPS = 120

vec = pg.Vector2(0, -1)

while True:
    screen.fill(pg.Color('orange'))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    pg.draw.line(screen, pg.Color)

    pg.display.update()
    clock.tick(FPS)
