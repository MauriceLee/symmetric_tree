import math

binary_tree = [1, 2, 2, 3, 4, 4, 3]

lens = len(binary_tree)
n = 0

while lens > 0:
    binary = math.pow(2, n)
    lens = lens - binary
    count = binary / 2
    print(count)
    x = int(binary - 1)
    y = 2 * x
    
    while count >= 1:
        if binary_tree[x] != binary_tree[y]:
            print(False)
        else:
            x += 1
            y -= 1
            print(True)
        count -= 1
            
    n += 1