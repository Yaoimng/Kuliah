n = int(input())
for i in range(1, n+1):
    if i%10 == 0:
        continue
    elif i%42 == 0:
        print("ERROR")
        break
    else:
        print(i)
        
        