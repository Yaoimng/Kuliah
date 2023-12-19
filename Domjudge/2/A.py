# def 

# p,q = map(int, input().split())
# peta = [
#     "###############",
#     "##E.....#######",
#     "#######......##",
#     "#######......##",
#     "##......#######",
#     "##......#######",
#     "#######......##",
#     "#######......##",
#     "##......#######",
#     "##......#######",
#     "#######......##",
#     "#######......##",
#     "##......#######",
#     "##..........S##",
#     "###############",
# ]

def cari_jalan(peta, x, y, arah):
    if peta[y][x] == "E":
        return True

    if arah == 0:
        if x < len(peta[0]) - 1 and peta[y][x + 1] != "#":
            return cari_jalan(peta, x + 1, y, arah + 1)

    if arah == 1:
        if x > 0 and peta[y][x - 1] != "#":
            return cari_jalan(peta, x - 1, y, arah + 1)

    if arah == 2:
        if y < len(peta) - 1 and peta[y + 1][x] != "#":
            return cari_jalan(peta, x, y + 1, arah + 1)

    if arah == 3:
        if y > 0 and peta[y - 1][x] != "#":
            return cari_jalan(peta, x, y - 1, arah + 1)

    return False

def main():
    p, q = map(int, input().split())
    peta = []
    for i in range(q):
        peta.append(list(input()))

    xs, ys = peta.index("S"), peta[0].index("S")

    if "S" not in peta or "E" not in peta:
        print("tempat mulai atau tempat tujuan tak tergambar")
        return

    arah = 0
    while not cari_jalan(peta, xs, ys, arah):
        arah = arah + 1

    for i in range(q):
        for j in range(p):
            if peta[i][j] == "S" or peta[i][j] == "E":
                continue

            if arah % 4 == 0:
                peta[i][j] = "x"
            elif arah % 4 == 1:
                peta[i][j] = "x"
            elif arah % 4 == 2:
                peta[i][j] = "x"
            elif arah % 4 == 3:
                peta[i][j] = "x"

    for line in peta:
        print("".join(line))

if __name__ == "__main__":
    main()




