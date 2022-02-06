# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:33:51 2022

@author: Netanel Iyov
"""
import numpy as np

# function to decide wether assigning x to P[r][c] is valid 
def isValid (P,r,c,x): 
    for y in P[r]:
        if (y==x):
            return False
    for i in range (9):
        if(P[i][c] == x and i!=r):
            return False
    
    u=r%3
    d=3-u
    
    le=c%3
    ri=3-le
    
    for i in range(r-u,r+d):
        for j in range(c-le, c+ri):
            if(P[i][j]==x and i!=r and j!=c):
                return False
    
    return True


def Solve(P,r,c):
    # Base cases
    # 1st Base case: if we reached end of row, recursivly call the function on the next row 
    if (r<8 and c>8):
        Solve(P,r+1,0)
    # 2nd Base case: if we reached end of last row, then the sudoku puzzle is solved. Print it 
    elif (r==8 and c>8):
        print (np.array(P))
        return
    
    else:
        if (P[r][c]==0):                     # if its an uninitialized value then do the following 
            for n in range (1,10):           # for all possible values, check if their valid
                  if(isValid(P,r,c,n)):      # if theres a valid value for P[r][c] then assign it 
                      P[r][c]=n              # and recursivly call the function on the next box in this row
                      Solve(P,r,c+1)         
                  
                      P[r][c]=0              # if we returned from the recursive call before Puzzle was solves then this value does not fit - then uninitialize it
        else:                                
            Solve(P,r,c+1)                   # if it is not an empty cell then recursivly execute next cell
        
    return
    


P =       [[0, 0, 6, 8, 0, 0, 0, 0, 3],
           [3, 0, 0, 0, 0, 0, 0, 5, 1],
           [0, 0, 1, 3, 4, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0],
           [9, 0, 5, 0, 0, 7, 3, 4, 0],
           [6, 0, 0, 2, 5, 0, 1, 0, 7],
           [0, 0, 4, 5, 0, 0, 0, 0, 9],
           [5, 0, 0, 0, 0, 2, 0, 0, 0],
           [0, 0, 0, 0, 7, 9, 0, 8, 0]]

#Solve(myBoard,0,0)
P= (Solve(P,0,0))

