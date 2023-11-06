a,b = input().split()
a = int(a)
b = int(b)
ganjil = 0

for i in range(a, b+1):
    if i % 2 == 1:
        ganjil += i

print(ganjil)