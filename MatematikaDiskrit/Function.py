def main():
    print("Pilih Fungsi: \n")
    print('1. Tower Hanoi \n')
    print('2. Deret Aritmatika \n')
    x = int(input())
    if x == 1:
        return hanoi()
    elif x == 2:
        return aritmatika()
    else:
        print("Angka yang anda masukkan salah")
        break