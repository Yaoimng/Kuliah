N = int(input())
best_price = None
best_quality = None
for i in range(N):
    item = input().split()
    ID, nama_item, harga, kualitas = map(str, item)

    harga = int(harga)
    kualitas = int(kualitas)

    if best_price is None or harga < best_price[2] or (harga == best_price[2] and ID < best_price[0]):
        best_price = (ID, nama_item, harga, kualitas)

    if best_quality is None or kualitas > best_quality[3] or (kualitas == best_quality[3] and ID < best_quality[0]):
        best_quality = (ID, nama_item, harga, kualitas)

print(f"Best item for price is: {' '.join(map(str, best_price))}")
print(f"Best item for quality is : {' '.join(map(str, best_quality))}")