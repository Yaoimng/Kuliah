N = int(input())
handphones = []
for _ in range(N):
    handphones.append(input())

M = int(input())
mappings = []
for _ in range(M):
    hp1, hp2 = input().split()
    
    idx1 = handphones.index(hp1)
    idx2 = handphones.index(hp2)
    
    handphones[idx1], handphones[idx2] = handphones[idx2], handphones[idx1]

for hp in handphones:
    print(hp)

