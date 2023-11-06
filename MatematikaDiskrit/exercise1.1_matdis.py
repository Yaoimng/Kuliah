def implication(p,q):
      return (not p) or q
def exclusive_disjunction(p, q):
    return (p and not q) or (not p and q)
def bi_implication(p, q):
  return p == q
def disjunction(p, q):
  return (p or q)
def conjunction(p, q):
  return (p and q)

# 37 A
# print("p      q       r    (-q v r)    p → (¬q ∨ r)")
# for p in [True, False]:
#   for q in [True, False]:
#     for r in [True, False]:
#       qr = disjunction(not q, r)
#       print(f"{p}  {q}  {r}  {not q or r}  {implication(p, qr)} ")
      
# 37 b
# print("p      q       r    -p     (q → r)   -p → (q → r)")
# for p in [True, False]:
#   for q in [True, False]:
#     for r in [True, False]:
#       qr = implication(q, r)
#       print(f"{p}  {q}  {r}  {(not p)} {implication(q, r)}  {implication(p, qr)} ") 

# 37 C
# print("p      q       r    (p → q)     (-p → r)   (p → q) v (-p → r)")
# for p in [True, False]:
#   for q in [True, False]:
#     for r in [True, False]:
#       pq = implication(p, q)
#       pr = implication(not p, r)
#       print(f"{p}  {q}  {r}  {pq} {pr}  {pq or pr} ")

# 37 D
# print("p      q       r    (p → q)     (-p → r)   (p → q) ^ (-p → r)")
# for p in [True, False]:
#   for q in [True, False]:
#     for r in [True, False]:
#       pq = implication(p, q)
#       pr = implication(not p, r)
#       print(f"{p}  {q}  {r}  {pq} {pr}  {pq and pr} ")

# 37 E
# print("p      q       r    (p ↔ q)     (-q ↔ r)   (p ↔ q) v (-q ↔ r)")
# for p in [True, False]:
#   for q in [True, False]:
#     for r in [True, False]:
#       pq = bi_implication(p, q)
#       qr = bi_implication(not q, r)
#       print(f"{p}  {q}  {r}  {pq} {qr}  {pq or qr} ")

# 37 F
# print("p      q       r    (-p ↔ -q)     (q ↔ r)   (-p ↔ -q) ↔ (q ↔ r)")
# for p in [True, False]:
#   for q in [True, False]:
#     for r in [True, False]:
#       pq = bi_implication(not p,not q)
#       qr = bi_implication(q, r)
#       print(f"{p}  {q}  {r}  {pq} {qr}  {bi_implication(pq, qr)} ")

# # 42 A
# x = 1
# if x + 2 == 3:
#   x = x + 1
# print(x)
  
# # 42 B
# x = 1
# if (x + 1 == 3) or (2*x + 2 == 3):
#   x = x + 1
# print(x)

# # 42 C
# x = 1
# if (2*x + 3 == 5) and (3*x + 4 == 7):
#   x = x + 1
# print(x)

# # 42 D
# x = 1
# p = (x + 1 == 2)
# q = (x + 2 == 3)
# if exclusive_disjunction(p, q):
#   x = x + 1
# print(x)

# # 42 E
# x = 1
# if x < 2:
#   x = x + 1
# print(x)