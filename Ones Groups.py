#!/bin/python3
#In a square grid, two cells are connected if they share an edge and share the same value. Sharing an edge is up, down, left and right, 
#but not diagonal. Given a square grid, determine the number of cells in each connected group of values. There will be an array of queries, each one an integer. 
#Create a return array of integers where each element is the number of groups in the matrix that have a size that matches the query.


import math
import os
import random
import re
import sys


#
# Complete the 'onesGroups' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY grid
#  2. INTEGER_ARRAY queries
#

def onesGroups(grid, queries):
    #print(grid,"\n")
    local_count = 0
    #print(queries)
    n = len(queries)
    res = []
    counts = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j]==1):
                local_count = local_count + countfunc(grid,i,j)
                counts.append(local_count)
            local_count = 0    
            
            #print(grid[i][j], end=" ")
        #print()    
    # Write your code here
    print (counts)
    
    for b in queries:
        res.append(counts.count(b))
    
    return res
                
def countfunc(grid,row,col):
    if any([row<0,col<0,row>=len(grid),col >= len (grid[0])]):
        return 0
    if grid[row][col]==0:
        return 0
    
    cell_count = 1
    grid[row][col] = 0
    for r in range(row-1, row+2):
        for c in range(col-1,col+2):
            if any([r!=row,c!=col]):
                if any([r == row, c ==col]):
                    cell_count += countfunc(grid,r,c)
    return cell_count
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = onesGroups(grid, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
