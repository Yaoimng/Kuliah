n = int(input())

angka = list(map(int, input().split()))

maks = angka[0]
min = angka[0]

for i in range(n):
    if angka[i] > maks:
        maks = angka[i]
    if angka[i] < min:
        min = angka[i]
print(maks,min)