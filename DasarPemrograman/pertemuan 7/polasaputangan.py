n = int(input())
a = 0

# increasing portion of the pattern
for i in range(1, n+2):
    # print space
    for j in range(i, n+1):
        print(" ", end=" ")
    # print digit
    for k in range(1, 2*i):
        if k < i:
            print(a, end=" ")
            a += 1
        elif k == i:
            print(a, end=" ")
        else:
            a -= 1
            print(a, end=" ")
    # new line
    print()

# decreasing portion of the pattern
for i in range(n, 0, -1):
    # print space
    for j in range(n, i-1, -1):
        print(" ", end=" ")
    # print digit
    for k in range(1, 2*i):
        if k < i:
            print(a, end=" ")
            a += 1
        elif k == i:
            print(a, end=" ")
        else:
            a -= 1
            print(a, end=" ")
    # new line
    print()

