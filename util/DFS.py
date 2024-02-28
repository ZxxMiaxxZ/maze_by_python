from queue import LifoQueue
import pygame
from maze import Maze
import time

class DFSSolver:
    def DFS(m,goal_position):
        start=(10,10)
        explored=[start]
        frontier=[start]
        dfsPath={}
        dSeacrh=[]
        visited_nodes =0
        
        start_time = time.time()
        
        while len(frontier)>0:
            currCell=frontier.pop()
            visited_nodes += 1  
            dSeacrh.append(currCell)
            if currCell==goal_position:
                break
            poss=0
            for d in ['right', 'left', 'top', 'bottom']:
                if m.maze_map_run[currCell][d] == 1:
                    if d == 'right':
                        child = (currCell[0], currCell[1] + 1)
                    elif d == 'left':
                        child = (currCell[0], currCell[1] - 1)
                    elif d == 'top':
                        child = (currCell[0] - 1, currCell[1])
                    elif d == 'bottom':
                        child = (currCell[0] + 1, currCell[1])
                    if child in explored:
                        continue
                   
                    explored.append(child)
                    frontier.append(child)
                    dfsPath[child]=currCell
        end_time = time.time()
        execution_time = end_time - start_time
        
        fwdPath={}
        cell=goal_position
        while cell!=start:
            fwdPath[dfsPath[cell]]=cell
            cell=dfsPath[cell]
        result_list = list(fwdPath.values())
        result_list = list(reversed(result_list))
        # print("Visited Nodes:", visited_nodes) 

        return result_list,fwdPath,dSeacrh, visited_nodes, execution_time
   