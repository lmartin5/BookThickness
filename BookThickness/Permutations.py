"""Permutations.py
@author lmartin5

This file contains the functions create permutations of the spine ordering
of numbers 1 - n for the book embedding problem. These permuations are then used 
with BookThickness.py to search for n-page book embeddings of graphs.
"""

def get_spines(n):
    """
    Main function for generating the permutations
    Parameters:
        n: an integer, permutations created will be 1, 2, ... , n
    Returns:
        spines: a list of all possible spine orderings (ignoring flip and rotation elements)
               if n is the integer, n!/2n permutations will be returned
    """
    spines = []
    generate_permutations(n, spines)
    spines = remove_dihedral_elements(spines)
    spines = [string_to_perm(spine) for spine in spines]
    return spines

def find_and_remove_flip(line, lines):
    reverse = line[::-1]
    try:
        del lines[reverse]
    except:
        return

def find_and_remove_rotations(line, lines):
    rotation = line

    for i in range(len(line) - 1):
        rotation = rotation[-1] + rotation[0:-1]
        try:
            del lines[rotation]
        except:
            return

def find_and_remove_dihedrals(line, lines):
    rotation = line
    find_and_remove_flip(line, lines)

    for i in range(len(line) - 1):
        rotation = rotation[-1] + rotation[0:-1]
        try:
            del lines[rotation]
        except:
            pass
        flip = rotation[::-1]    
        try:
            del lines[flip]
        except:
            return

def remove_dihedral_elements(perms):
    perms_dict = store_perms_in_dict(perms)
    count = 0
    for perm_value in list(perms_dict):
        if perm_value in perms_dict:
            find_and_remove_dihedrals(perm_value, perms_dict)
            count = count + 1        
    perms = list(perms_dict.values())
    return perms

# Function to store permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def generate_perm(a, l, r, perms):
    if l==r:
        perms.append(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            generate_perm(a, l+1, r, perms)
            a[l], a[i] = a[i], a[l] # backtrack

# This code is contributed by Bhavya Jain
def generate_permutations(num_elements, perms):
    string = ""
    for i in range(1, num_elements + 1):
        if i < 10:
            string += str(i)
        else:
            string += chr(i + 87)

    n = len(string)
    a = list(string)
    
    generate_perm(a, 0, n-1, perms)

def toString(List):
    return ''.join(List)

def strings_to_perms(perms):
    for i in range(len(perms)):
        perms[i] = string_to_perm(perms[i])
    return perms

def perm_to_string(perm):
    printed = ""
    for num in perm:
        if num < 10: 
            printed += str(num)
        else:
            printed += str(chr(num + 87))
    return printed

def string_to_perm(stri):
    perm = []
    for character in stri:
        if character.isnumeric():
            perm.append(int(character))
        else:
            perm.append(ord(character) - 87)
    return perm

def store_perms_in_dict(perms):
    new_perms = dict([])
    for perm in perms:
        new_perms[perm] = perm
    return new_perms