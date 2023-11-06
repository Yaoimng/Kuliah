tahun = int(input())

if tahun < 1900 or tahun >9000:
    print("Tahun di luar batas")

hari = ['sabtu','minggu','senin','selasa','rabu','kamis','jumat']

x = (tahun + (tahun // 4) - (tahun // 100) + (tahun // 400)) % 7

print(hari[x])
