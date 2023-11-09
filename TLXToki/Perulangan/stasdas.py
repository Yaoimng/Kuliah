def minimum(a):
    min = a[0]
    for i in range(0, len(a)):
        if a[i] < min:
            min = a[i]
    return min  

def maximum(a):
    max = a[0]
    for i in range(0, len(a)):
        if a[i] > max:
            max = a[i]
    return max

_ = int(input())
x = list(map(int,input().split()))
max = max(x)
min = min(x)
print (f"{max} {min}")
