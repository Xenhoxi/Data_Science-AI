import pygame
import numpy as np
import random
import os
import time


class Snake:
	def __init__(self, screen, width = 50, color=(100,0,100), grid_size=10):
		self.x = random.randint(2, 7)
		self.y = random.randint(2, 7)
		self.dir = self.random_dir()
		self.grid_size = grid_size
		self.grid = np.zeros((grid_size, grid_size))
		self.grid[self.x][self.y] = 1
		self.set_snake_on_grid(self.x, self.y)
		self.set_apple_on_grid()
		self.width = width
		self.color = color
		self.screen = screen
		self.img_head = pygame.image.load(os.path.join("game/snake_head.png"))

	
	def set_apple_on_grid(self):
		pass


	def set_snake_on_grid(self, x, y):
		if self.dir == 'UP':
			self.grid[x + 1, y] = 2
			self.grid[x + 2, y] = 3
		if self.dir == 'DOWN':
			self.grid[x - 1, y] = 2
			self.grid[x - 2, y] = 3
		if self.dir == 'LEFT':
			self.grid[x, y + 1] = 2
			self.grid[x, y + 2] = 3
		if self.dir == 'RIGHT':
			self.grid[x, y - 1] = 2
			self.grid[x, y - 2] = 3


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
		for x in range(self.grid_size):
			for y in range(self.grid_size):
				if self.grid[y, x] == 1:
					self.screen.blit(self.img_head, (x * self.width, y * self.width))
				elif self.grid[y, x] > 1:
					pygame.draw.rect(self.screen, self.color,
							   (x * self.width, y * self.width, self.width, self.width))
		

	def find_head(self):
		for x in range(self.grid_size):
			for y in range(self.grid_size):
				if self.grid[y, x] == 1:
					return x, y
				

	def find_tail(self):
		max = self.grid.max()
		for x in range(self.grid_size):
			for y in range(self.grid_size):
				if self.grid[y, x] == max:
					return x, y


	def add_1_to_grid(self):
		for x in range(self.grid_size):
			for y in range(self.grid_size):
				if self.grid[y, x] >= 1:
					self.grid[y, x] += 1


	def move(self):
		if not self.dir:
			return
		y, x = self.find_head()
		self.add_1_to_grid()
		if self.dir == 'UP':
			if x - 1 >= 0:
				self.grid[x - 1, y] = 1
		if self.dir == 'DOWN':
			if x + 1 < self.grid_size:
				self.grid[x + 1, y] = 1
		if self.dir == 'LEFT':
			if y - 1 >= 0:
				self.grid[x, y - 1] = 1
		if self.dir == 'RIGHT':
			if y + 1 < self.grid_size:
				self.grid[x, y + 1] = 1
		x, y = self.find_tail()
		self.grid[y, x] = 0
		

	def is_dead(self):
		for x in range(self.grid_size):
			for y in range(self.grid_size):
				if self.grid[y, x] == 1:
					return 0
		return 1


	def change_move(self, key):
		if key == pygame.K_UP and self.dir != 'DOWN':
			self.dir = 'UP'
		if key == pygame.K_DOWN and self.dir != 'UP':
			self.dir = 'DOWN'
		if key == pygame.K_LEFT and self.dir != 'RIGHT':
			self.dir = 'LEFT'
		if key == pygame.K_RIGHT and self.dir != 'LEFT':
			self.dir = 'RIGHT'

	def print_grid(self, key):
		if key == pygame.K_i:
			print(f"Grid: {self.dir}")
			print(self.grid)
