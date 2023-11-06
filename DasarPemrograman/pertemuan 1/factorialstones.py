import math 

n = int(input())
x = math.factorial(n)
count = 0
#print(x)
while x % 10 == 0:
    count+=1
    x //= 10
print(count)
if count%4 ==0 :
    print('Tuker dulu Rink!')
else:
    print('gas pol rem blong, Rink!')