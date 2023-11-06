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
def conjunction2(p, q, r):
    return (p and q and r)

#10 conditional statements is a tautology

#10 a
# print("p      q     ¬p      (p ∨ q)     ( ¬p ∧ (p ∨ q))   ((¬p ∧ (p ∨ q)) → q)")
# for p in [True, False]:
#   for q in [True, False]:
#     pq = disjunction(p, q)
#     ppq = conjunction(not p, pq)
#     ppqq = implication(ppq, q)
#     print(f"{p}  {q}  {not p}     {pq}      {ppq}           {ppqq} ")
# if ppqq [True]:
#   print('Berarti tautology')

#10b
# print("p      q     r      (p → q)     (q → r)   (p → r)     [(p → q) ∧ (q → r)] → (p → r)")
# for p in [True, False]:
#   for q in [True, False]:
#       for r in [True, False]:
#         pq = implication(p, q)
#         qr = implication(q, r)
#         pr = implication(p, r)
#         pqqr = conjunction(pq, qr)
#         pqr = implication(pqqr, pr)
#         print(f"{p}  {q}  {r}  {pq} {qr}  {pr}  {pqr} ")
# print('Jadi [(p → q) ∧ (q → r)] → (p → r) merupakan tautology')

#10c
# print("p      q     (p → q)     [p ∧ (p → q)]     [p ∧ (p → q)] → q")
# for p in [True, False]:
#   for q in [True, False]:
#     pq = implication(p, q)
#     ppq = conjunction(p, pq)
#     ppqq = implication(ppq, q)
#     print(f"{p}  {q}    {pq}            {ppq}               {ppqq}")
# print('Jadi [p ∧ (p → q)] → q merupakan tautology')

#10d
# print("p      q     r      (p ∨ q)      (p → r)    (q → r)      [(p ∨ q) ∧ (p → r) ∧ (q → r)]    [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r")
# for p in [True, False]:
#   for q in [True, False]:
#       for r in [True, False]:
#         pq = disjunction(p, q)
#         pr = implication(p, r)
#         qr = implication(q, r)
#         pqr = conjunction2(pq, pr, qr)
#         pqrr = implication(pqr, r)
#         print(f"{p}  {q}  {r}   {pq}        {pr}        {qr}                    {pqr}                               {pqrr}")
# print('Jadi [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r merupakan tautology')

#32 logically not equivalent
x = {}
print("p      q     r      (p ∧ q)     (p → r)     (q → r)      (p ∧ q) → r      (p → r) ∧ (q → r)")
for p in [True, False]:
  for q in [True, False]:
      for r in [True, False]:
        pq = conjunction(p, q)
        pqr = implication(pq, r)
        pr = implication(p, r)
        qr = implication(q, r)
        prqr = conjunction(pr, qr)
        print(f"{p}  {q}  {r}   {pq}        {pr}        {qr}                    {pqr}                               {prqr}")
        if pr and qr:
          print("equivalent")
          x = {'equivalent'}
        else:
          print("tidak equivalent")
          x = {'tidak equivalent'}
print(x)

