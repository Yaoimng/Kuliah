soal_benar = int(input())
waktu = input()

waktu_arr = waktu.split(' ')

jam = int(waktu_arr[0])
menit = int(waktu_arr[1])
detik = int(waktu_arr[2])

nilai = soal_benar * 4 - (25 - soal_benar)
lebih_jam = 9 - jam
lebih_menit = 59 - menit
lebih_detik = 59 - detik

if (soal_benar >= 5 and menit >= 7 and detik >= 30):
    menit_to_detik = menit * 60 + detik
    lebihan = menit_to_detik // (7 * 6 + 30)
    nilai += lebihan * 2
    
