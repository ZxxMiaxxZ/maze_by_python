from queue import PriorityQueue
import pygame
from maze import Maze
import time

class DijkstraSolver:
    def dijkstra(m,goal_position):
        start =(10,10)
        open = PriorityQueue()
        open.put((0, start))
        dist = {cell: float('inf') for cell in m.maze_map_run}
        dist[start] = 0
        aPath = {}
        searchPath = [start]
        visited_nodes = 0  # Counter for visited nodes

        start_time = time.time()
        
        while not open.empty():
            currCost, currCell = open.get()
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

                    edgeCost = 1  # Assuming each step has a cost of 1

                    if dist[currCell] + edgeCost < dist[childCell]:
                        dist[childCell] = dist[currCell] + edgeCost
                        open.put((dist[childCell], childCell))
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
        # print("Visited Nodes:", visited_nodes)  # Print the visited nodes count

        return result_list, fwdPath, searchPath,visited_nodes, execution_time

# Example usage:
# dijkstra_solver = DijkstraSolver()
# result, path, search_path = dijkstra_solver.dijkstra(maze_object, start_position, goal_position)
# print(result)
# print(path)
# print(search_path)
