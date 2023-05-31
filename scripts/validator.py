from models.molecule import Molecule

# function to validate the sequences composition
def sequencesValidator(sequence1:str, sequence2:str):
    #check if both sequences are the same type

    if isDNA(sequence1.upper()) and isDNA(sequence2.upper()):
        return True
    if isRNA(sequence1.upper()) and isRNA(sequence2.upper()):
        return True
    if isAminoAcid(sequence1.upper()) and isAminoAcid(sequence2.upper()):
        return True

# validates if sequences are DNA
def isDNA(sequence:str):
    molecule = Molecule()
    for char in sequence:
        if not char in molecule.DNA:
            return False
    return True

# validates if sequences are RNA
def isRNA(sequence:str):
    molecule = Molecule()
    for char in sequence:
        if not char in molecule.RNA:
            return False
    return True

# validates if sequences are Amino Acid
def isAminoAcid(sequence:str):
    molecule = Molecule()
    for char in sequence:
        if not char in molecule.aminoAcid:
            return False
    return True

    