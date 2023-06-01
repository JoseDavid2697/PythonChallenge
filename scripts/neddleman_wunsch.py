# Logic to solve the aligment
# according to the Neddleman-Wunsch algorithm

import sys

# Initialize variables
# --------------------
SAME = 2 # diagonal
DIFF = -1 # diagonal
GAP = -2 # down - right
MATRIX = []
#---------------------

def fillMatrix(sequence1:str, sequence2:str):
    global MATRIX
    x = len(sequence2)
    y = len(sequence1)
    s1 = []
    s2 = []

    for letter in sequence1:
        s1.append(letter)
    for letter in sequence2:
        s2.append(letter)

    #starting matrix with in wich values are going to be inserted 
    MATRIX = [[0 for i in range(y+1)] for j in range(x+1)]

    # comparison values
    for r in range(1, x+1):
        listOfValues = []
        value = 0
        result = 0
        for c in range(1, y+1):
            if s2[r-1] == s1[c-1]:
                value = SAME
            else:
                value = DIFF
            
            # addition
            #
            # diagonal 
            result = MATRIX[r-1][c-1] + value
            listOfValues.append(result)
            # right
            result = MATRIX[r][c-1] + GAP
            listOfValues.append(result)
            # down
            result = MATRIX[r-1][c] + GAP
            listOfValues.append(result)

            MATRIX[r][c] = max(listOfValues)
            listOfValues = []
        

def aligment(sequence1:str, sequence2:str):
    #print matrix
    fillMatrix(sequence1, sequence2)
    for line in MATRIX:
        print(line)
    
