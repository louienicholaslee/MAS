import random

print("100")

permutation = [x for x in range(100)]
random.shuffle(permutation)

i = 0
while i < 100:
    j = 0
    while j < 100:
        if permutation.index(j) > permutation.index(i):
            print("1 "),
        else:
            print("0 "),
        j += 1
    print
    i += 1
