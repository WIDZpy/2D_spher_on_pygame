import math as mt
import pygame as pg


class Sphere:
	def __init__(self, surface, distance, center=(200, 200), color=None, color_fond=None, shape=300, width1=1):

		self.win = surface
		self.distence = distance
		self.color1 = (255, 255, 255) if color_fond is None else color_fond
		self.color2 = (255, 255, 255) if color is None else color
		self.win.fill(self.color1)
		self.sphere_shape = shape
		# self.winsize = pg.display.get_window_size()
		self.width1 = width1
		self.position = center
		# pg.draw.ellipse(self.win, self.color1, (winsize[0]/2-shape/2, winsize[1]/2-shape/2, shape, shape), self.width1)

	def draw_parallel(self, repetition=range(-90, 91, 5)):
		# triengle abc rectengle en a
		for angle in repetition:
			angle = mt.radians(angle)
			cb = self.sphere_shape/2
			ba = cb * mt.sin(angle)
			ca = mt.cos(angle) * cb
			b = (self.position[0] + ca-3, self.position[1] + ba)
			bprime = (self.position[0] - ca+1, self.position[1] + ba)
			# print(cb, ba, ca, b, bprime)
			pg.draw.aaline(self.win, self.color2, b, bprime)

	def draw_meridian(self, repetition=range(0, 91, 5)):
		for angle in repetition:
			angle = mt.radians(angle)
			de = 2 * (mt.sin(angle) * self.sphere_shape/2)
			pg.draw.ellipse(self.win, self.color2, (self.position[0] - de/2, self.position[1] - self.sphere_shape/2,
				de, self.sphere_shape), self.width1)
			print(de, self.width1)


if __name__ == '__main__':
	run = True
	winsize = (512, 512)
	clock = pg.time.Clock()
	pg.init()
	win = pg.display.set_mode(winsize)

	spher = Sphere(win, distance=100, color=(255, 0, 0), color_fond=(0, 0, 0))

	spher.draw_parallel(range(-90, 91, 7))
	spher.draw_meridian(range(0, 91, 7))
	while run:
		# pg.time.delay(16)  # 33ms ~= 30fps | 16ms ~= 60fps | multi-threading and gpu accel to be made, might not be needed
		if pg.event.get(pg.QUIT):
			run = False
		clock.tick(100)
		pg.display.update()

