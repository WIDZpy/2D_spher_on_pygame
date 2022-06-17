import pygame as pg
import math as mh

pi = mh.pi

win = pg.display.set_mode((600, 600))

pg.draw.arc(win, (255, 255, 255), (0, 0, 100, 200), pi, pi+0.3)

run = True
compteur = 0
while run:
	compteur += 0.1
	pg.time.delay(100)
	if pg.event.get(pg.QUIT):
		run = False
	pg.draw.arc(win, (255, 255, 255), (10, 10, 100, 200), pi*3/2, pi/2)
	pg.display.update()