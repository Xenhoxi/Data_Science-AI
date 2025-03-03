import pygame
import numpy as np


class Snake:
	def __init__(self, screen, width = 50, color=(0,0,210), grid_size=10):
		self.x = 0
		self.y = 0
		self.dir = None
		self.grid = np.full((grid_size, grid_size), '0', dtype=str)
		self.grid[self.x][self.y] = 'H'
		self.width = width
		self.color = color
		self.screen = screen


	def draw(self):
		pygame.draw.rect(self.screen, self.color,
				   (self.x * self.width, self.y * self.width, self.width, self.width))
		

	def move(self, key):
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
			print(f"Grid:")
			print(self.grid)
