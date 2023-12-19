def insertsort(a,n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j-1], a[j]
                
