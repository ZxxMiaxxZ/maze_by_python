from queue import PriorityQueue
import pygame
from maze import Maze
import time

class AStarSolver:
    def h(cell1, cell2):
        x1, y1 = cell1
        x2, y2 = cell2
        return abs(x1 - x2) + abs(y1 - y2)

    def aStar(m,goal_position):
        # start = (10,10)
        start = (10,10)
        open = PriorityQueue()
        open.put((AStarSolver.h(start, goal_position), AStarSolver.h(start, goal_position), start))
        aPath = {}
        g_score = {cell: float('inf') for cell in m.maze_map_run}
        g_score[start] = 0
        f_score = {cell: float('inf') for cell in m.maze_map_run}
        f_score[start] = AStarSolver.h(start, goal_position)
        searchPath=[start]
        visited_nodes = 0 
        
        start_time = time.time()
        
        while not open.empty():
            currCell = open.get()[2]
            visited_nodes += 1  # Increment the visited nodes counter
            searchPath.append(currCell)
            if currCell == goal_position:
                break        
            for d in ['right', 'bottom', 'top', 'left']:
                if m.maze_map_run[currCell][d]==True:
                    if d=='right':
                        childCell=(currCell[0],currCell[1]+1)
                    elif d=='left':
                        childCell=(currCell[0],currCell[1]-1)
                    elif d=='top':
                        childCell=(currCell[0]-1,currCell[1])
                    elif d=='bottom':
                        childCell=(currCell[0]+1,currCell[1])

                    temp_g_score = g_score[currCell] + 1
                    temp_f_score = temp_g_score + AStarSolver.h(childCell, goal_position)

                    if temp_f_score < f_score[childCell]:   
                        g_score[childCell] = temp_g_score
                        f_score[childCell] = temp_g_score + AStarSolver.h(childCell, goal_position)
                        open.put((f_score[childCell], AStarSolver.h(childCell, goal_position), childCell))
                        aPath[childCell] = currCell

        end_time = time.time()
        execution_time = end_time - start_time
        
        fwdPath={}
        cell=goal_position
        while cell!=start:
            fwdPath[aPath[cell]]=cell
            cell=aPath[cell]
        result_list = list(fwdPath.values())
        result_list = list(reversed(result_list))        
        print("Visited Nodes:", visited_nodes)  # Print the visited nodes count

        return result_list,fwdPath,searchPath,visited_nodes, execution_time

        print(fwdPath)
        print()
        print(aPath)
        print()
        print(searchPath)
        # return fwdPath
 