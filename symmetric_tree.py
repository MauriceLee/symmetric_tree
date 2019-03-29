import math

def isSymmetric(root):
    lens = len(root)
    n = 0
    while lens > 0:
        binary = math.pow(2, n)
        lens = lens - binary
        count = binary / 2
        x = int(binary - 1)
        y = 2 * x
        while count >= 1:
            if root[x] != root[y]:
                return False
            else:
                x += 1
                y -= 1
            count -= 1
        n += 1
    return True

def main():
    root = [1, 2, 2, 3, 4, 4, 3]
    result = isSymmetric(root)
    print(result)

if __name__ == '__main__':
    main()
