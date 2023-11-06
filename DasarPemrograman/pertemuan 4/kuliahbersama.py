import re

_ = input()
days  = [int(x) for x in re.split(r" +", input())]
last = input()

day = ["senin", "selasa", "rabu", "kamis", "jumat","sabtu", "minggu"]

#fpb
def fpb(*number):
    a = number[0]
    for b in number[1:]:
        while b != 0:
            a, b = b, a % b
    return a

def kpk(*number):
    res = number[0]
    for n in number[1:]:
        res = res * n // fpb(res, n)
    return res

print(day[{day.index(last) + kpk(*days)}%7])
        