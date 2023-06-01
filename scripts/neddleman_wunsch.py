# Logic to solve the aligment
# according to the Neddleman-Wunsch algorithm

import sys

# Initialize variables
# --------------------
SAME = 2 # diagonal
DIFF = -1 # diagonal
GAP = -2 # down - right
MATRIX = []
s1 = []
s2 = []
sequenceLength = 0
equalsResidue = 0
sequenceIdentity = 0
#---------------------

def traceback():
    global MATRIX
    global s1
    global s2
    global equalsResidue
    global sequenceLength
    global sequenceIdentity
    # loop matrix
    x = len(s2)
    y = len(s1)
    upperList = []
    middleList = []
    lowerList = []

    # r, c define rows and colums so the last value of the MATRIX is M[r][c]
    r = x
    c = y
    run = True
    output = ""
    while run:
        if r >= 1 and c >= 1:
            # get neighbours values
            listN = []
            upperN = MATRIX[r-1][c]
            listN.append(upperN)
            leftN = MATRIX[r][c-1]
            listN.append(leftN)
            diagonalN = MATRIX[r-1][c-1]
            listN.append(diagonalN)
            # compare values
            # if values are equal
            if s1[y-1] == s2[x-1]:
                # move in diagonal
                upperList.append(str(s1[y-1]))
                middleList.append("|")
                lowerList.append(str(s2[x-1]))
                r -= 1
                c -= 1
                x -= 1
                y -= 1
                equalsResidue += 1
            else:
                # look for max value
                maxValue = max(listN)
                if diagonalN == maxValue:
                    #move diagonal
                    upperList.append(str(s1[y-1]))
                    middleList.append(" ")
                    lowerList.append(str(s2[x-1]))
                    r -= 1
                    c -= 1
                    x -= 1
                    y -= 1
                elif leftN == maxValue:
                    #move left
                    upperList.append(str(s1[y-1]))
                    middleList.append(" ")
                    lowerList.append("_")
                    c -= 1
                    y -= 1
                elif upperN == maxValue:
                    #move upper
                    output = "_" + "\n" + " " + "\n" + s2[x-1] + "\n" + output
                    upperList.append("_")
                    middleList.append(" ")
                    lowerList.append(str(s2[x-1]))
                    r -= 1
                    x -= 1
        else:
            run = False    
    print("==============================================") 
    print(upperList)
    print(middleList)
    print(lowerList)
            
        
            


def fillMatrix(sequence1:str, sequence2:str):
    global MATRIX
    global s1
    global s2
    x = len(sequence2)
    y = len(sequence1)

    print(sequence1)
    print(sequence2)

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
    
    traceback()
    print(equalsResidue)
    
