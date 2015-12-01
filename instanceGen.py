# This creates an instance where the ideal ranking is some permutation of 1,2,...,100
# Note that node P(1) points to P(2),...,P(100). P(k) points to only P(k+1),...,P(100)
# Note that this graph is a cycle where each P(i) points to P(i+1) including P(100),
# which points to P(1)

import random

sol = open("solution.txt", "w")
instance = open("instance1.txt", "w")

def genSimple(n):
    instance.write(str(n) + "\n")

    permutation = [x for x in range(n)]
    random.shuffle(permutation)
    for perm in permutation:
        sol.write(str(perm + 1))
        sol.write(" ")
    sol.close()
 
    i = 0
    while i < n:
        j = 0
        while j < n:
            if permutation.index(j) > permutation.index(i):
                instance.write("1 ")
            elif (permutation[n-1] == i) and (permutation[0] == j):
                instance.write("1 ")
            else:
                instance.write("0 ")
            j += 1
        instance.write("\n")
        i += 1
    instance.close()
    return

genSimple(100)
