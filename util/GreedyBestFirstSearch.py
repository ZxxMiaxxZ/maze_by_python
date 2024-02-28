from queue import PriorityQueue
import pygame
from maze import Maze
import time

class GreedySolver:
    def h(cell, goal_position):
        x, y = cell
        goal_x, goal_y = goal_position
        return abs(x - goal_x) + abs(y - goal_y)

    def greedy(m, goal_position):
        start = (10,10)
        open = PriorityQueue()
        open.put((GreedySolver.h(start, goal_position), start))
        aPath = {}
        searchPath = [start]
        visited_nodes = 0  
        
        start_time = time.time()
        
        while not open.empty():
            _, currCell = open.get()
            visited_nodes += 1  # Increment the visited nodes counter
            searchPath.append(currCell)

            if currCell == goal_position:
                break

            for d in ['right', 'bottom', 'top', 'left']:
                if m.maze_map_run[currCell][d]:
                    if d == 'right':
                        childCell = (currCell[0], currCell[1] + 1)
                    elif d == 'left':
                        childCell = (currCell[0], currCell[1] - 1)
                    elif d == 'top':
                        childCell = (currCell[0] - 1, currCell[1])
                    elif d == 'bottom':
                        childCell = (currCell[0] + 1, currCell[1])

                    if childCell not in aPath:
                        open.put((GreedySolver.h(childCell, goal_position), childCell))
                        aPath[childCell] = currCell
        end_time = time.time()
        execution_time = end_time - start_time
        
        fwdPath = {}
        cell = goal_position
        while cell != start:
            fwdPath[aPath[cell]] = cell
            cell = aPath[cell]
        result_list = list(fwdPath.values())
        result_list = list(reversed(result_list))

        return result_list, fwdPath, searchPath, visited_nodes, execution_time

