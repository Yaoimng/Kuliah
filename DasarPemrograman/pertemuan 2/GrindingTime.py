N = int(input())

abyss = N // 10
hilichurl = 0
slime = 0

N = N % 10
if 8 < N <= 10:
    N -= 10
    abyss += 1
elif 6 < N <= 8:
    N -= 8
    hilichurl += 1
else :
    N -= 6
    slime += 1

total_damage = slime * 3 + hilichurl * 4 + abyss * 5
print(total_damage)
print(slime)
print(hilichurl)
print(abyss)