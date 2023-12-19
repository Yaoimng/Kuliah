def cetakA (baris, kolom):
    for a in range (baris):
        if ((a+1) % 2 == 1): print(" ", end="")
        for c in range (kolom):
            if ((c+1) % 2 == 1): print(".", end="")
            else : print("-", end="")
        print()
        
    
def cetakB (baris,  kolom):
    for b in range(baris):
        if ((b+1) % 2 == 0): print(" ", end="")
        for k in range(kolom):
            if ((k+1) % 2 == 0): print(".", end="")
            else :
                print("-", end="")
        print()

testcase = int(input())
for t in range(testcase):
    list_input = input().split()
    
    patern = list_input[0]
    baris = int(list_input[1])
    kolom = int(list_input[2])
    if patern == "A":
        cetakA(baris, kolom)
    else :
        cetakB(baris, kolom)
