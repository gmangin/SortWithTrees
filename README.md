 ____             _ __        ___ _   _   _____
 / ___|  ___  _ __| |\ \      / (_) |_| |_|_   _| __ ___  ___  ___
 \___ \ / _ \| '__| __\ \ /\ / /| | __| '_ \| || '__/ _ \/ _ \/ __|
  ___) | (_) | |  | |_ \ V  V / | | |_| | | | || | |  __/  __/\__ \
  |____/ \___/|_|   \__| \_/\_/  |_|\__|_| |_|_||_|  \___|\___||___/
                                                                    

====================================================================

A little challenge with my solution in python ;) 


## DESCRIPTION

Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order in between trees and without moving the trees.

# Example
```
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortWithTrees(a) = [-1, 150, 160, 170, -1, -1, 160, 180].
```

# Input/Output

  * [execution time limit] 4 seconds (python3)

  * [input] array.integer a

```If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

 Guaranteed constraints:
5 ≤ a.length ≤ 15,
-1 ≤ a[i] ≤ 200.
```

  * [output] array.integer

```Sorted array between each trees a with all the trees untouched.```

