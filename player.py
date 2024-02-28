import pygame
from maze import Maze
import time
class Player:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y) 
		self.player_size = 30
		self.rect = pygame.Rect(self.x, self.y, self.player_size, self.player_size)
		self.velX = 0
		self.velY = 0
		self.left_pressed = False
		self.right_pressed = False
		self.up_pressed = False
		self.down_pressed = False
		self.speed = 30

	# stops player to pass through walls
	def check_move(self, tile,maze_map_run ,thickness):
		current_cell_x, current_cell_y = self.y // tile, self.x // tile
		current_cell_abs_x, current_cell_abs_y = current_cell_y * tile, current_cell_x * tile
		
		print("Player:", self.y, self.x)
		print("Current Cell:", current_cell_x, current_cell_y)		
		
		if self.left_pressed:
			print("Checking Left:", maze_map_run[current_cell_x, current_cell_y]['left'])

			if maze_map_run[current_cell_x,current_cell_y]['left'] == 0:				
					self.left_pressed = False
		if self.right_pressed:
			print("Checking Right:", maze_map_run[current_cell_x, current_cell_y]['right'])

			if maze_map_run[current_cell_x,current_cell_y]['right'] == 0:
					self.right_pressed = False
		if self.up_pressed:
			print("Checking Top:", maze_map_run[current_cell_x, current_cell_y]['top'])
			
			if maze_map_run[current_cell_x,current_cell_y]['top'] == 0:
					self.up_pressed = False
		if self.down_pressed:
			print("Checking Bottom:", maze_map_run[current_cell_x, current_cell_y]['bottom'])

			if maze_map_run[current_cell_x,current_cell_y]['bottom'] == 0:
					self.down_pressed = False




	# drawing player to the screen
	def draw(self, screen, color):
		pygame.draw.rect(screen, color , self.rect)



	# updates player position while moving
	def update(self):
		self.velX = 0
		self.velY = 0
		if self.left_pressed and not self.right_pressed:
			self.velX = -self.speed
		if self.right_pressed and not self.left_pressed:
			self.velX = self.speed
		if self.up_pressed and not self.down_pressed:
			self.velY = -self.speed
		if self.down_pressed and not self.up_pressed:
			self.velY = self.speed

		self.x += self.velX
		self.y += self.velY

		self.rect = pygame.Rect(int(self.x), int(self.y), self.player_size, self.player_size)





	def follow_path(self,path,screen):
		
		path = list(reversed(path))
		if path:
			# 
			next_cell = path[-1]  # Get the next cell from the path
			target_x = next_cell[1] * self.speed
			target_y = next_cell[0] * self.speed

			# Move towards the target cell
			if self.x < target_x:
				self.velX = self.speed
			elif self.x > target_x:
				self.velX = -self.speed
			else:
				self.velX = 0

			if self.y < target_y:
				self.velY = self.speed
			elif self.y > target_y:
				self.velY = -self.speed
			else:
				self.velY = 0

			# If the player has reached the target cell, remove it from the path
			if self.x == target_x and self.y == target_y:
				path.pop()
			self.x += self.velX
			self.y += self.velY
			self.rect = pygame.Rect(int(self.x), int(self.y), self.player_size, self.player_size)
   
	def follow_searchPath(self, path, screen):
		self.velX = 0
		self.velY = 0
		# Check if the path is not empty
		if path:
			# Extract the target coordinates from the current step in the path
			target_y,target_x = path[0]
	
			target_x = target_x*30
			target_y = target_y*30

			# Move towards the target cell
			if self.x < target_x:
				temp = (target_x-self.x)/30
				self.velX = self.speed*temp
			elif self.x > target_x:
				temp = abs(target_x-self.x)/30
				self.velX = -self.speed*temp
			else:
				self.velX = 0

			if self.y < target_y:
				temp = abs(target_y-self.y)/30
				self.velY = self.speed*temp
			elif self.y > target_y:
				temp = abs(target_y-self.y)/30
				self.velY = -self.speed*temp
			else:
				self.velY = 0

			# If the player has reached the target cell, remove it from the path
			if self.x == target_x and self.y == target_y:
				path.pop(0)  # Remove the current step from the path

		# Rest of your code remains the same...

			self.x += self.velX
			self.y += self.velY
			# self.x = target_x
			# self.y = target_y
			self.rect = pygame.Rect(int(self.x), int(self.y), self.player_size, self.player_size)



			