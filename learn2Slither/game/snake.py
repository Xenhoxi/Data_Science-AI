import pygame
import numpy as np
import random


class Snake:
	def __init__(self, screen, width = 50, color=(0,0,210), grid_size=10):
		self.x = random.randint(0, 9)
		self.y = random.randint(0, 9)
		self.dir = self.random_dir()
		self.grid = np.zeros((grid_size, grid_size))
		self.grid[self.x][self.y] = 1
		self.width = width
		self.color = color
		self.screen = screen


	def random_dir(self):
		res = random.randint(0, 3)
		if res == 0:
			return 'LEFT'
		elif res == 1:
			return 'UP'
		elif res == 2:
			return 'RIGHT'
		elif res == 3:
			return 'DOWN'


	def draw(self):
		pygame.draw.rect(self.screen, self.color,
				   (self.x * self.width, self.y * self.width, self.width, self.width))
		

	def move(self):
		# if self.dir:
			# x, y = find_head()
			# x, y = find_tail()
		if self.dir == 'UP':
			pass
		if self.dir == 'DOWN':
			pass
		if self.dir == 'LEFT':
			pass
		if self.dir == 'RIGHT':
			pass
		

	def change_move(self, key):
		if key == pygame.K_UP:
			self.dir = 'UP'
		if key == pygame.K_DOWN:
			self.dir = 'DOWN'
		if key == pygame.K_LEFT:
			self.dir = 'LEFT'
		if key == pygame.K_RIGHT:
			self.dir = 'RIGHT'

	def print_grid(self, key):
		if key == pygame.K_i:
			print(f"Grid: {self.dir}")
			print(self.grid)
