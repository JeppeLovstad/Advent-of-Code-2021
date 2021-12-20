import sys
import numpy as np

output = 0
lines = []
path = sys.path[0]+"\input.txt"


with open(path, 'r', encoding='utf-8') as f:
    for l in f:
        l = l.rstrip()
        lines.append(list(l))

n = np.array(lines)

height = len(n)-1
width = len(n[0])-1

print(height,width)

low_points = 0
for i in range(height+1):
    for j in range(width+1):
        x_min = max(0,j-1)  
        x_max = min(width, j+1)
        y_min = max(0,i-1)  
        y_max = min(height, i+1)
        #print(x_min,x_max,y_min,y_max)
        
        cur_value = int(n[i,j])
        up = 99 if y_min != i-1 else int(n[i-1,j])
        down = 99 if y_max != i+1 else int(n[i+1,j])
        left = 99 if x_min != j-1 else int(n[i,j-1])
        right = 99 if x_max != j+1 else int(n[i,j+1])
        
        #print(i,j, cur_value, up, down, left, right)
        if cur_value < up and cur_value < down and cur_value < left and  cur_value < right:
            low_points += cur_value + 1
        
print(low_points)

def adj_finder(matrix, position):
    adj = []
    
    ranges = [
        [-1,0],
        [1,0],
        [0,-1],
        [0,1]
    ]
    
    for dx,dy in ranges:
        #for dy in range(-1, 2):
            #if dx == dy:
            #    continue
        rangeX = range(0, matrix.shape[1])  # X bounds
        rangeY = range(0, matrix.shape[0])  # Y bounds
        
        #print(rangeX, rangeY)
        
        (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell
        #print(newX, newY)
        
        if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
            adj.append((newX, newY))
    #print(position,adj)
    return adj

def plot_points(x,y,matrix,basin_dict,visited_points,basin_name):
    point_tuple = (x,y)
    if point_tuple in visited_points:
        return (basin_dict, visited_points)
    visited_points[point_tuple] = 1
    if int(matrix[y,x]) == 9:
        return (basin_dict, visited_points)
    #print(point_tuple,basin_name)
    
    basin_dict.setdefault(basin_name, []).append(point_tuple)
    #nb = adj_finder(n, point_tuple)
    #print(point_tuple,nb)
    for nb in adj_finder(matrix, point_tuple):
        #print(nb)
        if int(matrix[nb[1],nb[0]]) != 9:
            basin_dict,visited_points = plot_points(nb[0],nb[1],matrix,basin_dict,visited_points,basin_name)
    return (basin_dict,visited_points)
    

basin_dict = {}
visited_points = {}
for y in range(height):
    for x in range(width):
        basin_dict,visited_points = plot_points(x,y,n,basin_dict,visited_points,(x,y))
        
result2 = 1
lens = list(map(len,basin_dict.values()))
for k in sorted(lens)[-3:]:
    #print(result2)
    result2 =  result2*k
    #print(k, len(basin_dict[k]), basin_dict[k])
print(result2)
#print(basin_dict,visited_points)

#print(n)
#print(n[0:3,0:3])
