#!/usr/bin/python3

from sortWithTrees import sortWithTrees

def compar(list1, list2):
    for i in range(len(list1)): # assuming the lists are of the same length
        if list1[i]!=list2[i]:
            return False
    return True

def main():
    array1 = [-1, 150, 190, 170, -1, -1, 180, 160]
    answer1 = [-1, 150, 170, 190, -1, -1, 160, 180]
    res1 = sortWithTrees(array1)
    if compar(res1, answer1):
        print('true, ', res1)
        return 0
    else:
        print('False', res1)
        return -1
    

if __name__ == "__main__":
    main()
