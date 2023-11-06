waktu_awal = input()

waktu_arr = waktu_awal.split(':')

jam_awal = int(waktu_arr[0])
menit_awal = int(waktu_arr[1])
detik_awal = int(waktu_arr[2])

lama_perjalan = input()

lama_arr = lama_perjalan.split(' ')

jam_lama = int(lama_arr[0])
menit_lama = int(lama_arr[2])
detik_lama = int(lama_arr[4])

beda_waktu = input()
jam_beda = int(beda_waktu)

detik = detik_awal+detik_lama
menit = menit_awal+menit_lama+(detik // 60)
jam = jam_awal+jam_lama+jam_beda+(detik //60)

detik = detik%60
menit = menit%60
jam = jam%24

print(f'Mehas akan sampai pada pukul {jam}:{menit}:{detik} waktu setempat')