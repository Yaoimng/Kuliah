def copy_array(listangka, sizearray, destinasi, pos):
    for i in range(sizearray):
        destinasi[pos][i] = listangka[i]

def print_array(listangka, sizearray):
    for i in range(sizearray):
        print(listangka[i], end=' ')
    print()

def print_array_3d(listangka, sizearray, pos):
    for j in range(sizearray):
        print(listangka[pos][j], end=' ')
    print()

def pascal(listangka, sizearray, pos):
    if sizearray == 1:
        # print(listangka[0])
        pass
    else:
        pascallist = [0] * (sizearray - 1)
        for i in range(sizearray - 1):
            sum_val = listangka[i] + listangka[i + 1]
            pascallist[i] = sum_val

        copy_array(pascallist, sizearray - 1, hasilpascal, pos)
        pos += 1
        pascal(pascallist, sizearray - 1, pos)
        pos -= 1
        print_array_3d(hasilpascal, sizearray - 1, pos)

def pascal_full(listangka, sizearray):
    pascal(listangka, sizearray, 0)
    print_array(listangka, sizearray)

x = int(input())
listangka = list(map(int, input().split()))
hasilpascal = [[0] * 101 for k in range(101)]
pascal_full(listangka, x)