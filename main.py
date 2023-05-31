# Sequence Aligment
# Jose David Rodriguez
# Astrix, Associate Informatics Engineer
#
# This program is an approach to solve the sequence aligment problem
# using the Needleman-Wunsch algorithm

import os
from scripts.validator import sequencesValidator
from scripts.neddleman_wunsch import aligment

clear = lambda: os.system("cls")

# options menu
def menu():
    print("-- The program allow you to do sequence aligment using two input methods")
    print("-- Please select one of the following options\n")
    print("[1] Type or paste sequences")
    print("[2] Open files")
    print("[0] Exit the program")

# wait for an entry
menu()
print("\n")
option = int(input("Enter your option: "))

# Sequences
s1 = ""
s2 = ""


# funtions
# received the copied entry as input
def getInput():
    clear()
    print("Please provide the first sequence (you can paste it with CTRL+V)")
    sequence1 = str(input())
    print("Please provide the second sequence (you can paste it with CTRL+V)")
    sequence2 = str(input())
    equals = sequencesValidator(sequence1, sequence2)
    while equals != True:
        print("----- WARNING ----- \n Make sure sequences have the same type")
        print("Please provide the first sequence (you can paste it with CTRL+V)")
        sequence1 = str(input())
        print("Please provide the second sequence (you can paste it with CTRL+V)")
        sequence2 = str(input())
        equals = sequencesValidator(sequence1, sequence2)
    
    return True


def readFile():
    global s1
    global s2
    # open files
    file1 = open("docs/sequence1.txt", "r")
    file2 = open("docs/sequence2.txt", "r")

    s1 = file1.readlines()[0]
    s2 = file2.readlines()[0]
    clear()
    equals = sequencesValidator(s1, s2)
    if equals != True:
        print("----- WARNING ----- \n Make sure sequences have the same type!")
        return False
     
    return True

# display menu until option is received
while option != 0:
    if option == 1:
        #do option 1
        if getInput():
            print("Aligning please wait...")

    elif option == 2:
        #do option 2
        if readFile():
            print("Aligning please wait...")  
            aligment(s1, s2) 
            
    else:
        print("Invalid option")
    
    print()
    menu()
    option = int(input("Enter your option: "))
