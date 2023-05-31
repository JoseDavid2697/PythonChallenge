# Logic to solve the aligment
# according to the Neddleman-Wunsch algorithm

# Initialize variables
# --------------------
SAME = 2 # diagonal
DIFF = -1 # diagonal
GAP = -2 # down - right

#---------------------

def aligment(sequence1:str, sequence2:str):
    x = len(sequence2)
    y = len(sequence1)
    s1 = []
    s2 = []

    for letter in sequence1:
        s1.append(letter)
    for letter in sequence2:
        s2.append(letter)

    #starting matrix with in wich values are going to be inserted 
    MATRIX = [[0 for i in range(y)] for j in range(x)]

    # comparison values
    for i in range(x):
        listOfValues = []
        value = 0
        result = 0
        for j in range(y):
            if s2[i] == s1[j]:
                value = SAME
            else:
                value = DIFF
            
            # addition
            if i == 0 and j == 0:
                # diagonal
                result = value
                listOfValues.append(result)
                # right
                result = 0 + -2
                listOfValues.append(result)
                # down 
                result = 0 + -2
                listOfValues.append(result)
                # add the max to the list
                MATRIX[i][j] = max(listOfValues)
            
            

    for line in MATRIX:
        print(line)
    
