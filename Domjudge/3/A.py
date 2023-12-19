def f(n):
    if n == 1:
        print("*")
        return
    elif n == 2:
        print("**")
    else:
        f(n-2)
        print("*"* n)
        f(n-2)

n = int(input())
f(n)