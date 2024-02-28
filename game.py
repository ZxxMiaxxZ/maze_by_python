import pygame
import csv
from maze import Maze
pygame.font.init()

class Game:
	def __init__(self, goal_cell, tile):
		self.font = pygame.font.SysFont("impact", 35)
		self.message_color = pygame.Color("darkorange")
		self.tile = tile
		


	# add goal point for player to reach
	def add_goal_point(self, screen, goal_position):
		# adding gate for the goal point
		img_path = 'img/gate.png'
		img = pygame.image.load(img_path)
		img = pygame.transform.scale(img, (self.tile, self.tile))
		screen.blit(img, (goal_position[1] * self.tile, goal_position[0] * self.tile))

	# winning message
	def message(self):
		msg = self.font.render('Player 1 Win!!', True, self.message_color)
		return msg
	def message2(self):
		msg = self.font.render('Player 2 Win!!', True, self.message_color)
		return msg
	
	

	# checks if player reached the goal point
	def is_game_over(self, player,goal_position):

		 # Assuming there's a method in Maze to get the goal position
		goal_cell_abs_x, goal_cell_abs_y = goal_position[1] * self.tile, goal_position[0] * self.tile
		if player.x == goal_cell_abs_x and player.y == goal_cell_abs_y:
			return True
		return False