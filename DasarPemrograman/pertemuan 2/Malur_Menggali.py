def main():
    X, Y = map(int, input().split())
    a = []
    for i in range(Y):
        row = list(map(int, input().split()))
        a.append(row)
    
    s = int(input())
    # untuk mengantisipasiagar tidak mengakses array yang lebih
    ul = X - s + 1
    el = Y - s + 1
    output = 0

    for h in range(el):
        for i in range(ul):
            hasil = 0

            for j in range(s):
                for k in range(s):
                    hasil += a[j + h][k + i]


            if hasil >= output:
                output = hasil
    
    print(output)

if __name__ == "__main__":
    main()
