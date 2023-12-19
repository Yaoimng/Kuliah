def hitung_cara(n, kumpulan_angka):
    if n == 0:
        return 1
    jumlah_cara = 0

    for angka in kumpulan_angka:
        if angka <= n:
            jumlah_cara += hitung_cara(n - angka, kumpulan_angka)

    return jumlah_cara

syarat = [1, 3, 5]

S = int(input())

C = list(map(int, input().split()))

i = 1
for val in C:
    hasil = hitung_cara(val, syarat)
    print(f"SESI {i}: {hasil}") 
    i += 1