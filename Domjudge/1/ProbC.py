x = int(input())

if x <= 40:
    print("E")
elif x > 40 and x <=55:
    print("D")
elif x > 55 and x <=60:
    print("C")
elif x > 60 and x <=65:
    print("BC")
elif x > 65 and x <=75:
    print("B")
elif x > 75 and x <=85:
    print("AB")
elif x > 85 and x <=100:
    print("A")
else:
    print("input anda salah")