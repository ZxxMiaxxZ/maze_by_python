import pygame, sys, os
from maze import Maze
from player import Player
from game import Game
from clock import Clock
import time
from util.aStar import AStarSolver
from util.BFS import BFSSolver
from util.GreedyBestFirstSearch import GreedySolver
from util.dijkstra import DijkstraSolver
from util.DFS import DFSSolver
from random import randint
pygame.init()
pygame.font.init()

class Main():
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.SysFont("impact", 20)
		self.fonts = pygame.font.SysFont("impact", 15)
		self.tiltes = pygame.font.SysFont("impact", 40)
		self.message_color = pygame.Color("cyan")
		self.tiltes_color = pygame.Color("red")
		self.running = True
		self.game_over = False
		self.FPS = pygame.time.Clock()
		self.button_color = (255, 0, 0)
		self.goal_position = self.get_goal_position_random()
		self.goal_position2 = None
		self.loadmaze = 'maze1.csv'
		self.color_green = (0,255,0)
		self.color_red = (255,0,0)
		self.color_blue = (0,0,255)
		self.color_yellow = (255, 255, 0)
		self.winner = 0


	def instructions(self):
		#write group name & tiltes
		name_dang = self.fonts.render('Do Huynh Bao Dang', True, self.message_color)
		name_manh = self.fonts.render('Nguyen Duy Manh', True, self.message_color)
		name_truong = self.fonts.render('Do Xuan Truong', True, self.message_color)
		name_group = self.tiltes.render('Group 4', True,self.tiltes_color)
		#write 
		instructions1 = self.font.render('Use Arrow Keys', True, self.message_color)
		instructions2 = self.font.render('to Move', True, self.message_color)
		instructions3 = self.font.render('Time: ', True, self.message_color)
		instructions4 = self.tiltes.render('Algorithm ', True, self.color_yellow)
		instructions5 = self.tiltes.render('Other Funcion ', True, self.color_yellow)
		self.screen.blit(instructions1,(800,20))
		self.screen.blit(instructions2,(820,40))
		self.screen.blit(instructions3,(660,555))
		self.screen.blit(instructions4,(680,120))
		self.screen.blit(instructions5,(680,350))
		self.screen.blit(name_dang,(660,50))
		self.screen.blit(name_manh,(660,70))
		self.screen.blit(name_truong,(660,90))
		self.screen.blit(name_group,(655,0))
	#Draw button
		#Reset
		text1 = self.font.render("Reset", True, (255, 255, 255))
		pygame.draw.rect(screen, self.button_color, (660, 600, 100, 50))
		text1_rect = text1.get_rect(center=(660 + 100 // 2, 600 + 50 // 2))
		self.screen.blit(text1,text1_rect)
		#Alth button
		bfs_text = self.font.render("BFS", True, (255, 255, 255))
		pygame.draw.rect(screen, self.button_color, (660, 170, 100, 50))
		bfs_text_rect = bfs_text.get_rect(center=(660 + 100 // 2, 170 + 50 // 2))
		self.screen.blit(bfs_text,bfs_text_rect)
  
		dfs_text = self.font.render("DFS", True, (255, 255, 255))
		pygame.draw.rect(screen, self.button_color, (800, 170, 100, 50))
		dfs_text_rect = dfs_text.get_rect(center=(800 + 100 // 2, 170 + 50 // 2))
		self.screen.blit(dfs_text,dfs_text_rect)

		A_start_text = self.font.render("A*", True, (255, 255, 255))
		pygame.draw.rect(screen, self.button_color, (660, 230, 100, 50))
		A_start_text_rect = A_start_text.get_rect(center=(660 + 100 // 2, 230 + 50 // 2))
		self.screen.blit(A_start_text,A_start_text_rect) 

		Greedy_text = self.font.render("Greedy", True, (255, 255, 255))
		pygame.draw.rect(screen, self.button_color, (800, 230, 100, 50))
		Greedy_text_rect = Greedy_text.get_rect(center=(800 + 100 // 2, 230 + 50 // 2))
		self.screen.blit(Greedy_text,Greedy_text_rect)
  
		Dijkstra_text = self.font.render("Dijkstra", True, (255, 255, 255))
		pygame.draw.rect(screen, self.button_color, (660, 290, 100, 50))
		Dijkstra_text_rect = Dijkstra_text.get_rect(center=(660 + 100 // 2, 290 + 50 // 2))
		self.screen.blit(Dijkstra_text,Dijkstra_text_rect)
  
		Change_map_text = self.font.render("Change Map", True, (0, 255, 0))
		pygame.draw.rect(screen, self.button_color, (800, 400, 100, 50))
		Change_map_text_rect = Change_map_text.get_rect(center=(800 + 100 // 2, 400 + 50 // 2))
		self.screen.blit(Change_map_text,Change_map_text_rect)

		Two_player_text = self.font.render("2 player", True, (0, 255, 0))
		pygame.draw.rect(screen, self.button_color, (660, 400, 100, 50))
		Two_player_text_rect = Two_player_text.get_rect(center=(660 + 100 // 2, 400 + 50 // 2))
		self.screen.blit(Two_player_text,Two_player_text_rect)

		Two_bot_text = self.font.render("Bot-Bot", True, (0, 255, 0))
		pygame.draw.rect(screen, self.button_color, (660, 460, 100, 50))
		Two_bot_text_rect = Two_bot_text.get_rect(center=(660 + 100 // 2, 460 + 50 // 2))
		self.screen.blit(Two_bot_text,Two_bot_text_rect)

		# Player_bot_text = self.font.render("Player-Bot", True, (0, 255, 0))
		# pygame.draw.rect(screen, self.button_color, (800, 460, 100, 50))
		# Player_bot_text_rect = Player_bot_text.get_rect(center=(800 + 100 // 2, 460 + 50 // 2))
		# self.screen.blit(Player_bot_text,Player_bot_text_rect)
  
	def get_goal_position_random(self):
		last_position = None  # Initialize with a default value
		r = randint(1, 4)  # Fix: Use randint instead of random and correct the range
		if r == 1:
			last_position = (1, 1)
		elif r == 2:
			last_position = (1, 20)
		elif r == 3:
			last_position = (20, 1)
		elif r == 4:
			last_position = (20, 20)

		return last_position

	# draws all configs; maze, player, instructions, and time
	def _draw(self, maze, tile, player, game, clock,color):

		# draw maze
		maze.draw_walls(screen, tile)
		# add a goal point to reach1111
		game.add_goal_point(self.screen,self.goal_position)

		# draw every player movement
		player.draw(self.screen,color)
		player.update()
		
		# instructions, clock, winning message
		self.instructions()
		if self.game_over:
			clock.stop_timer()
			self.screen.blit(game.message(),(660,520))
			
		else:
			clock.update_timer()
		self.screen.blit(clock.display_timer(), (710,550))
	
		pygame.display.flip()
  
  	# draws all configs; maze, player, instructions, and time
	def _drawTwoPlayer(self, maze, tile, player,player2, game, clock, color, color2):

		# draw maze
		maze.draw_walls(screen, tile)
		# add a goal point to reach1111
		game.add_goal_point(self.screen,self.goal_position)
		if(self.goal_position2 != None):
			game.add_goal_point(self.screen,self.goal_position2)

		# draw every player movement
		player.draw(self.screen,color)
		player.update()
		
		player2.draw(self.screen,color2)
		player2.update()
		
		# instructions, clock, winning message
		self.instructions()
		if self.game_over:
			if self.winner == 0:
				clock.stop_timer()
				self.screen.blit(game.message(),(660,520))
			elif self.winner == 1:
				clock.stop_timer()
				self.screen.blit(game.message2(),(660,520))
		else:
			clock.update_timer()
		self.screen.blit(clock.display_timer(), (710,550))
	
		pygame.display.flip()
 



	# main game loop
	def main(self, frame_size, tile):
		cols, rows = frame_size[0] // tile, frame_size[1] // tile
		maze = Maze(cols, rows)

		game = Game((4, 4), tile)  # Replace (4, 4) with your desired goal cell position
		player = Player(30*10,30*10)
		player2 = None
		clock = Clock()
		
		# maze.upload_map(loadMaze='maze3.csv')
		maze.upload_map(self.loadmaze)

		clock.start_timer()
		
		while self.running:
			self.screen.fill("gray")
			self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if not self.game_over:
        				 # Player 1
						if event.key == pygame.K_LEFT:
							player.left_pressed = True
							time.sleep(0.2)
       
						elif event.key == pygame.K_RIGHT:
							player.right_pressed = True
							time.sleep(0.2)

						elif event.key == pygame.K_UP:
							player.up_pressed = True
							time.sleep(0.2)

						elif event.key == pygame.K_DOWN:
							player.down_pressed = True
							time.sleep(0.2)

						player.check_move(tile,maze.maze_map_run,maze.thickness)

						# Player 2
						if(player2 != None):
							if event.key == pygame.K_a:
								player2.left_pressed = True
								time.sleep(0.2)

							elif event.key == pygame.K_d:
								player2.right_pressed = True
								time.sleep(0.2)


							elif event.key == pygame.K_w:
								player2.up_pressed = True
								time.sleep(0.2)
		

							elif event.key == pygame.K_s:
								player2.down_pressed = True
								time.sleep(0.2)
							player2.check_move(tile,maze.maze_map_run,maze.thickness)


				elif event.type == pygame.KEYUP:
					if not self.game_over:
						#Player 1
						if event.key == pygame.K_LEFT:
							player.left_pressed = False
						elif event.key == pygame.K_RIGHT:
							player.right_pressed = False
						elif event.key == pygame.K_UP:
							player.up_pressed = False
						elif event.key == pygame.K_DOWN:
							player.down_pressed = False
						player.check_move(tile,maze.maze_map_run,maze.thickness)
   						#Player 2
						if(player2 != None):
							if event.key == pygame.K_a :
								player2.left_pressed = False
							elif event.key == pygame.K_d:
								player2.right_pressed = False
							elif event.key == pygame.K_w:
								player2.up_pressed = False
							elif event.key == pygame.K_s:
								player2.down_pressed = False
							player2.check_move(tile,maze.maze_map_run,maze.thickness)



				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_x, mouse_y = pygame.mouse.get_pos()
					# Event Reset button
					if 660 <= mouse_x <= 660 + 100 and \
							600 <= mouse_y <= 600 + 50:
						player = Player(30*10,30*10)
						player2 = None
						clock.start_timer()
						self.goal_position = self.get_goal_position_random()
						self.game_over = False
						self.winner = 0
						self.goal_position2 = None
					# Event BFS button
					if 660 <= mouse_x <= 660 + 100 and \
							170 <= mouse_y <= 170 + 50:
						clock.start_timer()
						player = Player(30*10,30*10)
						player1 = Player(30*10,30*10)

						#-------------------------------------------
						bfs_path, bfs_fwdPath, bSearch, visited_nodes, execution_time = BFSSolver.BFS(maze, self.goal_position)

						font = pygame.font.Font(None, 36)
						text1 = font.render(f'Visited Nodes: {visited_nodes}', True, (0, 0, 0))
						screen.blit(text1, (50,650))
						text2 = font.render(f'Execution time (ms): {execution_time*1000:.5f}', True, (0, 0, 0))
						screen.blit(text2, (50,670))
	
						for step in bSearch:
							player1.follow_searchPath([step], self.screen)
							self._draw(maze, tile, player1, game, clock,self.color_blue)
							pygame.time.delay(10)
							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
						for step in bfs_fwdPath:
							player.follow_searchPath([step], self.screen)
							self._draw(maze, tile, player, game, clock,self.color_green)
							pygame.time.delay(100)
							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
						for step in bfs_path:
							if game.is_game_over(player,self.goal_position):
								self.game_over = True
							else:
								self.game_over = False
								player.follow_searchPath([step], self.screen)
								self._draw(maze, tile, player, game, clock,self.color_red)
								pygame.time.delay(100)
								self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						self.game_over = True
							
# -----------------------------------------------------------------------------

							

# -----------------------------------------------------------------------------

						print('BFS')
					# Event DFS button
					if 800 <= mouse_x <= 800 + 100 and \
							170 <= mouse_y <= 170 + 50:
						clock.start_timer()
						player = Player(30*10,30*10)
						player1 = Player(30*10,30*10)
						dfs_path, dfs_fwdPath, dfsSearch, visited_nodes, execution_time  = DFSSolver.DFS(maze, self.goal_position)

						font = pygame.font.Font(None, 36)
						text1 = font.render(f'Visited Nodes: {visited_nodes}', True, (0, 0, 0))
						screen.blit(text1, (50,650))
						text2 = font.render(f'Execution time (ms): {execution_time*1000:.5f}', True, (0, 0, 0))
						screen.blit(text2, (50,670))

						for step in dfsSearch:
							player1.follow_searchPath([step], self.screen)
							self._draw(maze, tile, player1, game, clock,self.color_blue)
							pygame.time.delay(10)
							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
						for step in dfs_fwdPath:
							player.follow_searchPath([step], self.screen)
							self._draw(maze, tile, player, game, clock,self.color_green)
							pygame.time.delay(100)
							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
						for step in dfs_path:
							if game.is_game_over(player,self.goal_position):
								self.game_over = True
							else:
								self.game_over = False
								player.follow_searchPath([step], self.screen)
								self._draw(maze, tile, player, game, clock,self.color_red)
								pygame.time.delay(100)
								self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						self.game_over = True

						print('DFS')
					# Event A* button
					if 660 <= mouse_x <= 660 + 100 and \
							230 <= mouse_y <= 230 + 50:
						clock.start_timer()
						player = Player(30*10,30*10)
						player1 = Player(30*10,30*10)
						astar_path, astar_fwdPath, AstarSearch, visited_nodes, execution_time = AStarSolver.aStar(maze, self.goal_position)
      
						font = pygame.font.Font(None, 36)
						text1 = font.render(f'Visited Nodes: {visited_nodes}', True, (0, 0, 0))
						screen.blit(text1, (50,650))
						text2 = font.render(f'Execution time (ms): {execution_time*1000:.5f}', True, (0, 0, 0))
						screen.blit(text2, (50,670))
      
						for step in AstarSearch:
							player1.follow_searchPath([step], self.screen)
							self._draw(maze, tile, player1, game, clock,self.color_blue)
							pygame.time.delay(10)
							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
						for step in astar_fwdPath:
							player.follow_searchPath([step], self.screen)
							self._draw(maze, tile, player, game, clock,self.color_green)
							pygame.time.delay(100)
							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
						for step in astar_path:
							if game.is_game_over(player,self.goal_position):
								self.game_over = True
							else:
								self.game_over = False
								player.follow_searchPath([step], self.screen)
								self._draw(maze, tile, player, game, clock,self.color_red)
								pygame.time.delay(100)
								self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						self.game_over = True
						print('A*')
					# Event Greedy button
					if 800 <= mouse_x <= 800 + 100 and \
							230 <= mouse_y <= 230 + 50:
						clock.start_timer()
						player = Player(30*10,30*10)
						player1 = Player(30*10,30*10)
						greedy_path, greedy_fwdPath, GreedySearch, visited_nodes, execution_time = GreedySolver.greedy(maze, self.goal_position)
      
						font = pygame.font.Font(None, 36)
						text1 = font.render(f'Visited Nodes: {visited_nodes}', True, (0, 0, 0))
						screen.blit(text1, (50,650))
						text2 = font.render(f'Execution time (ms): {execution_time*1000:.5f}', True, (0, 0, 0))
						screen.blit(text2, (50,670))
      
						for step in GreedySearch:
							player1.follow_searchPath([step], self.screen)
							self._draw(maze, tile, player1, game, clock,self.color_blue)
							pygame.time.delay(10)
							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
						for step in greedy_fwdPath:
							player.follow_searchPath([step], self.screen)
							self._draw(maze, tile, player, game, clock,self.color_green)
							pygame.time.delay(100)
							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
						for step in greedy_path:
							if game.is_game_over(player,self.goal_position):
								self.game_over = True
							else:
								self.game_over = False
								player.follow_searchPath([step], self.screen)
								self._draw(maze, tile, player, game, clock,self.color_red)
								pygame.time.delay(100)
								self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						self.game_over = True
						print('Greedy')
      				# Event Dijikstra button
					if 660 <= mouse_x <= 660 + 100 and \
							290 <= mouse_y <= 290 + 50:
						clock.start_timer()
						player = Player(30*10,30*10)
						player1 = Player(30*10,30*10)
						dijk_path, dijk_fwdPath, dijk_Search, visited_nodes, execution_time = DijkstraSolver.dijkstra(maze, self.goal_position)
      
						font = pygame.font.Font(None, 36)
						text1 = font.render(f'Visited Nodes: {visited_nodes}', True, (0, 0, 0))
						screen.blit(text1, (50,650))
						text2 = font.render(f'Execution time (ms): {execution_time*1000:.5f}', True, (0, 0, 0))
						screen.blit(text2, (50,670))
      
						for step in dijk_Search:
							player1.follow_searchPath([step], self.screen)
							self._draw(maze, tile, player1, game, clock,self.color_blue)
							pygame.time.delay(10)
							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
						for step in dijk_fwdPath:
							player.follow_searchPath([step], self.screen)
							self._draw(maze, tile, player, game, clock,self.color_green)
							pygame.time.delay(100)
							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
						for step in dijk_path:
							if game.is_game_over(player,self.goal_position):
								self.game_over = True
							else:
								self.game_over = False
								player.follow_searchPath([step], self.screen)
								self._draw(maze, tile, player, game, clock,self.color_red)
								pygame.time.delay(100)
								self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						self.game_over = True
						print('Dijkstra')
					# Event change map button
					if 800 <= mouse_x <= 800 + 100 and \
							400 <= mouse_y <= 400 + 50:
						clock.start_timer()
						if(self.loadmaze == 'maze1.csv'):
							maze.maze_map = []
							self.loadmaze = 'maze2.csv'
							maze.upload_map(self.loadmaze)
						elif(self.loadmaze == 'maze2.csv'):
							maze.maze_map = []
							self.loadmaze = 'maze3.csv'
							maze.upload_map(self.loadmaze)
						elif(self.loadmaze == 'maze3.csv'):
							maze.maze_map = []
							self.loadmaze = 'maze1.csv'
							maze.upload_map(self.loadmaze)
						print('Change Map')
					# Event draw 2 player button
					if 660 <= mouse_x <= 660 + 100 and \
							400 <= mouse_y <= 400 + 50:
						clock.start_timer()
						player2 = Player(30*11,30*11)
						print('Two player')
					# Event draw 2 bot button
					if 660 <= mouse_x <= 660 + 100 and \
							460 <= mouse_y <= 460 + 50:
						clock.start_timer()
						self.goal_position2 = self.get_goal_position_random()
						while (self.goal_position2 == self.goal_position):
							self.goal_position2 = self.get_goal_position_random()
						player2 = Player(30*10,30*10)
						greedy_path, greedy_fwdPath, GreedySearch = GreedySolver.greedy(maze, self.goal_position)
						greedy_path2, greedy_fwdPath2, GreedySearch2 = GreedySolver.greedy(maze, self.goal_position2)
						for step, step2 in zip(greedy_path, greedy_path2):
							player.follow_path([step], self.screen)
							player2.follow_path([step2], self.screen)
							self._drawTwoPlayer(maze, tile, player,player2, game, clock,self.color_green,self.color_blue)
							pygame.time.delay(200)

							self.screen.fill(pygame.Color("darkslategray"), (650, 0, 752, 752))
						
							if game.is_game_over(player,self.goal_position) :
								self.game_over = True
							elif game.is_game_over(player2,self.goal_position2) :
								self.winner = 1
								self.game_over = True
							else:
								self.game_over = False
					print('Two bot')


			#check win
			if game.is_game_over(player,self.goal_position):
				self.game_over = True
				player.left_pressed = False
				player.right_pressed = False
				player.up_pressed = False
				player.down_pressed = False
				if(player2 != None):
					player2.left_pressed = False
					player2.right_pressed = False
					player2.up_pressed = False
					player2.down_pressed = False
			elif(player2 != None):
				if game.is_game_over(player2,self.goal_position):
					self.game_over = True
					player.left_pressed = False
					player.right_pressed = False
					player.up_pressed = False
					player.down_pressed = False
					player2.left_pressed = False
					player2.right_pressed = False
					player2.up_pressed = False
					player2.down_pressed = False
					self.winner = 1
				elif( self.goal_position2 != None):
					if game.is_game_over(player2,self.goal_position2):
						self.game_over = True
						player.left_pressed = False
						player.right_pressed = False
						player.up_pressed = False
						player.down_pressed = False
						player2.left_pressed = False
						player2.right_pressed = False
						player2.up_pressed = False
						player2.down_pressed = False
					else:
						self.game_over = False
				else:
					self.game_over = False

			if(player2 == None):
				self._draw(maze,tile,player,game,clock,self.color_green)
			else:
				self._drawTwoPlayer(maze ,tile,player,player2 ,game, clock, self.color_green, self.color_blue)
			self.FPS.tick(60)



if __name__ == "__main__":
	window_size = (800, 720)
	screen = (window_size[0] + 150, window_size[-1])
	tile_size = 30
	screen = pygame.display.set_mode(screen)
	pygame.display.set_caption("Maze")

	game = Main(screen)
	game.main(window_size, tile_size)