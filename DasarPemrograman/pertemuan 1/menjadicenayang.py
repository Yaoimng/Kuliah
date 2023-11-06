tanggal = input()
tanggal_arr = tanggal.split(' ')

tgl = int(tanggal_arr[0])
bln = int(tanggal_arr[1])
thn = int(tanggal_arr[2])

K = thn % 100
J = thn // 100

hari = ['sabtu', 'minggu', 'senin', 'selasa', 'rabu', 'kamis', 'jumat']
h = (tgl + (13 * (bln + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)) % 7

match bln:
    case 1:
        bln = "januari"
    case 2:
        bln = "februari"
    case  3:
        bln = "maret"
    case 4:
        bln = "april"
    case 5:
        bln = "mei"
    case 6:
        bln = "juni"
    case 7:
        bln = "juli"
    case 8:
        bln = "agustus"
    case 9:
        bln = "september"
    case 10:
        bln = "oktober"
    case 11:
        bln = "november"
    case 12:
        bln = "desember"
        
print(f'Tanggal : {tgl} {bln} {thn}')
print(f'Hari : {hari[h]}')