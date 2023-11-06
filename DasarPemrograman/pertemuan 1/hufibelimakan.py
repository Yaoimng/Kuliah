n = int(input())

pecahan = [250, 100, 50, 20, 10, 5]
lembar = [0, 0, 0, 0, 0, 0]

if n>= pecahan[0]:
    lembar[0] = n // pecahan[0]
    n %= pecahan[0] 
    
if n>= pecahan[1]:
    lembar[1] = n // pecahan[1]
    n %= pecahan[1]
     
if n>= pecahan[2]:
    lembar[2] = n // pecahan[2]
    n %= pecahan[2] 
    
if n>= pecahan[3]:
    lembar[3] = n // pecahan[3]
    n %= pecahan[3] 
    
if n>= pecahan[4]:
    lembar[4] = n // pecahan[4]
    n %= pecahan[4] 
    
if n>= pecahan[5]:
    lembar[5] = n // pecahan[5]
    n %= pecahan[5] 

if n==0:
    for i in range(len(pecahan)):
        print(f'{lembar[i]} lembar {pecahan[i]} ribuan')
        
else:
    print('Harganya jelek :(')

