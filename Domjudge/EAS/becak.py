# Membaca input
n = int(input())
listmakanan = [input().split() for i in range(n)]

k, tipe = input().split()
k = int(k)

def sort_key(makanan):
    if tipe == 'S':
        return (makanan[0], -int(makanan[1]), -int(makanan[2]))
    elif tipe == 'P':
        return (-int(makanan[1]), -int(makanan[2]), makanan[0])
    elif tipe == 'Q':
        return (-int(makanan[2]), -int(makanan[1]), makanan[0])

sorted_listmakanan = sorted(listmakanan, key=sort_key)
for i in range(k):
    print(f"{sorted_listmakanan[i][0]} {sorted_listmakanan[i][1]} {sorted_listmakanan[i][2]}")
