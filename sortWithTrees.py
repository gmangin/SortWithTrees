#!/usr/bin/python3

def sortWithTrees(a):
    start = 0
    toOrder = False
    for i in range(len(a)):
        if a[i] != -1 and not toOrder:
            start = i
            toOrder = True
        elif a[i] == -1 and toOrder:
            a[start:i] = sorted(a[start:i])
            toOrder = False
        elif i == (len(a) - 1) and toOrder:
            a[start:] = sorted(a[start:])
    return a
