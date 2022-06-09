import math as mt
import pygame as pg


class Sphere:
	def __init__(self, window, distance, color1=None, color2=None, shape=(100, 100), width=1):
		self.color1 = [255, 255, 255] if color1 is None else color1
		self.color2 = [255, 255, 255] if color2 is None else color2
		self.shape = shape
		self.win = window
		self.winsize = pg.display.get_window_size()
		self.width = width
		pg.draw.ellipse(self.win, self.color1, (winsize[0]/2-shape[0]/2, winsize[1]/2-shape[1]/2, shape[0], shape[1]),
						self.width)


if __name__ == '__main__':
	run = True
	winsize = (512, 512)
	clock = pg.time.Clock()
	pg.init()
	win = pg.display.set_mode(winsize)
	spher = Sphere(win, 100)

	while run:
		# pg.time.delay(16)  # 33ms ~= 30fps | 16ms ~= 60fps | multi-threading and gpu accel to be made, might not be needed
		if pg.event.get(pg.QUIT):
			run = False
		clock.tick(100)
		pg.display.update()



