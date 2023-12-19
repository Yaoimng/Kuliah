def posisi_akashi(T, cases):
    results = []
    
    for i in range(T):
        N, K = cases[i]
        # Menghitung posisi Akashi menggunakan rumus modulus
        position = (N % K) + 1
        results.append(position)
    
    return results

# Membaca jumlah kasus
T = int(input())
cases = []

# Membaca input untuk setiap kasus
for _ in range(T):
    N, K = map(int, input().split())
    cases.append((N, K))

# Memanggil fungsi untuk menghitung posisi Akashi
hasil = posisi_akashi(T, cases)

# Menampilkan hasil untuk setiap kasus
for posisi in hasil:
    print(posisi)
