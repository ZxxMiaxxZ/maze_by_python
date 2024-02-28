from maze import Maze
import pygame
import time
from collections import deque

class BFSSolver:
    
    def BFS(m, goal_position):
        start = (10, 10)
        # start = goal_position
        frontier = deque()
        frontier.append(start)
        bfsPath = {}
        visited_nodes = 0  
        explored = [start]
        bSearch = []
        
        start_time = time.time()

        while len(frontier) > 0:
            currCell = frontier.popleft()
            visited_nodes += 1  
            if currCell == goal_position:
                break
            for d in ['right', 'bottom', 'top', 'left']:
                if m.maze_map_run[currCell][d] == True:
                    if d == 'right':
                        childCell = (currCell[0], currCell[1] + 1)
                    elif d == 'left':
                        childCell = (currCell[0], currCell[1] - 1)
                    elif d == 'top':
                        childCell = (currCell[0] - 1, currCell[1])
                    elif d == 'bottom':
                        childCell = (currCell[0] + 1, currCell[1])
                    if childCell in explored:
                        continue
                    frontier.append(childCell)
                    explored.append(childCell)
                    bfsPath[childCell] = currCell
                    bSearch.append(childCell)
        end_time = time.time()
        execution_time = end_time - start_time
        
        fwdPath = {}
        cell = goal_position

        fwdPath[bfsPath[cell]] = cell

        while cell != (10, 10):
            fwdPath[bfsPath[cell]] = cell
            cell = bfsPath[cell]

        
        result_list = list(fwdPath.values())
        result_list = list(reversed(result_list))

        return result_list, fwdPath, bSearch, visited_nodes, execution_time

