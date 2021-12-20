import sys
import numpy as np

output = 0
lines = []
path = sys.path[0]+"\input.txt"
with open(path, 'r', encoding='utf-8') as f:
    for l in f:
        l = map(int,l.rstrip())
        lines.append(list(l))

n = np.array(lines)
print(n)

def adj_finder(matrix, position):
    adj = []
    ranges = [
        [-1,0], #down
        [1,0],  #up
        [0,-1], #left
        [0,1],   #right
        [1,1],   #up-right
        [-1,-1], #down-left
        [-1,1],  #down-right
        [1,-1]  #up-left
    ]
    
    for dx,dy in ranges:
        rangeX = range(0, matrix.shape[1])  # X bounds
        rangeY = range(0, matrix.shape[0])  # Y bounds
        
        (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell
        if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
            adj.append((newX, newY))
    return adj

height = len(n)
width = len(n[0])
flat = n.flatten().tolist()
flashes=0
STEPS=0
while flat.count(flat[0]) != len(flat):
    already_flashed = {}
    
    ## increment all by one
    for y in range(0,height):
        for x in range(0,width):
            n[y,x] += 1
    
    
    ## find each element above 9
    for y in range(0,height):
        for x in range(0,width):
            point_tuple = (x,y)
            adjacent_above_9 = []
            
            ## if above 9 and not seen before, 
            ## increment flash counter and save node
            if n[y,x] > 9 and point_tuple not in already_flashed:
                already_flashed[point_tuple] = 1 
                flashes += 1
                
                ## get neighbours and check for any values above 9
                ## add to list to check later
                for nb in adj_finder(n,point_tuple):
                    n[nb[1],nb[0]] += 1 
                    if n[nb[1],nb[0]] > 9 and nb not in already_flashed:
                        adjacent_above_9.append(nb)
            
                ## for any neighbours above 9 repeat above process iteratively
                while len(adjacent_above_9) > 0:
                    curr_point_tuple = adjacent_above_9.pop() ## remember to remove element to continue
                    if curr_point_tuple in already_flashed:
                        continue
                    
                    already_flashed[curr_point_tuple] = 1 
                    flashes += 1
                
                    for nb in adj_finder(n,curr_point_tuple):
                        n[nb[1],nb[0]] += 1 
                        if n[nb[1],nb[0]] > 9 and nb not in already_flashed:
                            adjacent_above_9.append(nb)
                            
    ## stupid numpy doesnt have count                       
    flat = n.flatten().tolist()
    STEPS += 1
    
    ## part 1
    if STEPS == 100:
        print("part 1:", flashes)
    
    for x,y in already_flashed:
        n[y,x] = 0
    
print("part 2:", STEPS)
            
    