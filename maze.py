import pygame
import csv,os
import time
from random import randint


class Maze:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.thickness = 3
        self.maze_map = []
        self.maze_map_run = {}

    def upload_map(self, loadMaze):
        with open(loadMaze, 'r') as f:
            last = list(f.readlines())[-1]
            c = last.split(',')
            c[0] = int(c[0].lstrip('"('))
            c[1] = int(c[1].rstrip(')"'))
            self.rows = c[0]
            self.cols = c[1]
            # self.grid = []	
        with open(loadMaze, 'r') as f:
            r = csv.reader(f)
            next(r)
            for i in r:
                c = i[0].split(',')
                c[0] = int(c[0].lstrip('('))
                c[1] = int(c[1].rstrip(')'))
                
                self.maze_map.append({'position': tuple(c),'right': int(i[1]), 'left': int(i[2]), 'top': int(i[3]), 'bottom': int(i[4])})
                self.maze_map_run[tuple(c)]={'right':int(i[1]),'left':int(i[2]),'top':int(i[3]),'bottom':int(i[4])}                            

    def del_map(self,loadMaze):
        self.maze_map.append.clear()
        self.maze_map_run.clear()

            
    def get_last_position(self, loadMaze):
        last_position = None  # Initialize with a default value

        with open(loadMaze, 'r') as f:
            maze_data = list(csv.reader(f))
            last = maze_data[-1]
            last_position = tuple(map(int, last[0].strip('()"').split(',')))

            # Assuming there's a method in Maze to set rows, cols, and grid
            self.rows = last_position[0]
            self.cols = last_position[1]
            self.grid = []
        return last_position
    
    # def get_goal_position_random(self):
    #     last_position = None  # Initialize with a default value
    #     r = randint(1, 4)  # Fix: Use randint instead of random and correct the range
    #     if r == 1:
    #         last_position = (1, 1)
    #     elif r == 2:
    #         last_position = (20, 1)
    #     elif r == 3:
    #         last_position = (1, 20)
    #     elif r == 4:
    #         last_position = (20, 20)
        
    #     return last_position

            

    def draw_walls(self, screen, cell_size):
        wall_color = (0, 0, 0)
        path_color = (255, 0, 0)  # Color for the start position
        start_position = (10, 10)  # Set the start position here

        for cell_data in self.maze_map:
            position = cell_data['position']
            x, y = position[1] * cell_size, position[0] * cell_size
            if cell_data['top'] == 0:
                pygame.draw.line(screen, wall_color, (x, y), (x + cell_size, y), self.thickness)
            if cell_data['right'] == 0:
                pygame.draw.line(screen, wall_color, (x + cell_size, y), (x + cell_size, y + cell_size), self.thickness)
            if cell_data['bottom'] == 0:
                pygame.draw.line(screen, wall_color, (x, y + cell_size), (x + cell_size, y + cell_size), self.thickness)
            if cell_data['left'] == 0:
                pygame.draw.line(screen, wall_color, (x, y), (x, y + cell_size), self.thickness)
            if position == start_position:
                pygame.draw.rect(screen, path_color, (x, y, cell_size, cell_size), self.thickness)
                
        if start_position == self.get_last_position():
            pygame.draw.rect(screen, path_color, (x, y, cell_size, cell_size), self.thickness)   
            
    
    def draw_path(self, screen, cell_size, path):
        path_color = (0, 255, 0)  # Green color for the path
        path_thickness = 5

        for cell in path.values():
            x, y = cell[0] * cell_size, cell[1] * cell_size
            pygame.draw.rect(screen, path_color, (x, y, cell_size, cell_size), path_thickness)
            # time.sleep(0.5)

    def get_last_position(self):
            last_position = None

            if self.maze_map:
                last_position = self.maze_map[-1]['position']

            return last_position   

   
if __name__ == "__main__":
    pygame.init()
    window_size = (1080, 720)
    screen_size = (window_size[0] + 150, window_size[1])
    tile_size = 30
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Maze")

    # Create an instance of the Maze class with desired dimensions
    cols, rows = window_size[0] // tile_size, window_size[1] // tile_size
    maze = Maze(4, 4)

    maze.upload_map(loadMaze='maze1.csv')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Fill the screen with a white background
        maze.draw_walls(screen, tile_size)  # Draw the maze walls
        pygame.display.flip()

    pygame.quit()