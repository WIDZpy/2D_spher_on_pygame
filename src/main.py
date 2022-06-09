import math as mt
import pygame as pg


class Sphere:
	def __init__(self, window, distance, color1=None, color2=None, shape=300, width=1):
		self.win = window
		self.distence = distance
		self.color1 = [255, 255, 255] if color1 is None else color1
		self.color2 = [255, 255, 255] if color2 is None else color2
		self.sphere_shape = shape
		self.winsize = pg.display.get_window_size()
		self.width = width
		self.position = (winsize[0]/2, winsize[1]/2)
		pg.draw.ellipse(self.win, self.color1, (winsize[0]/2-shape/2, winsize[1]/2-shape/2, shape, shape), self.width)

	def draw_parallel(self, repetition=range(-90, 90, 5)):
		# triengle abc rectengle en a
		for angle in repetition:
			angle = mt.radians(angle)
			cb = self.sphere_shape/2
			ba = cb * mt.sin(angle)
			ca = mt.cos(angle) * cb
			b = (self.position[0] + ca-2, self.position[1] + ba)
			bprime = (self.position[0] - ca+1, self.position[1] + ba)
			print(cb, ba, ca, b, bprime)
			pg.draw.aaline(self.win, self.color2, b, bprime)


if __name__ == '__main__':
	run = True
	winsize = (512, 512)
	clock = pg.time.Clock()
	pg.init()
	win = pg.display.set_mode(winsize)
	spher = Sphere(win, 100)

	spher.draw_parallel(range(-90, 90, 7))
	while run:
		# pg.time.delay(16)  # 33ms ~= 30fps | 16ms ~= 60fps | multi-threading and gpu accel to be made, might not be needed
		if pg.event.get(pg.QUIT):
			run = False
		clock.tick(100)
		pg.display.update()

