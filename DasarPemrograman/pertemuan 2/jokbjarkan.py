Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Px, Py = map(int, input().split())

def cek_kuadran(x,y):
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3

a = cek_kuadran(Ax,Ay)
b = cek_kuadran(Bx,By)
c = cek_kuadran(Cx,Cy)

kuadran_arr = [a,b,c] 

if Px == Ax or Px == Bx or Px == Cx or Py == Ay or Py == By or Py == Cy:
    print("TITIK PENGAWAS: kuadran", " ".join(map(str, kuadran_arr)))
    print("KEPUNG BJARKAN!!!, DiaSegaris Dengan Kalian")
elif all(kuadran_arr.count(q) == 2 for q in kuadran_arr):
    print("TITIK PENGAWAS: kuadran", " ".join(map(str, kuadran_arr)))
    print("KEPUNG BJARKAN!!!, Tapi Dia Tidak Segaris Dengan Kalian")
elif all(kuadran_arr.count(q) == 1 for q in kuadran_arr):
    print("TITIK PENGAWAS: kuadran", " ".join(map(str, kuadran_arr)))
    print("Yo Ndak Tau Kok Tanya Saya")
else:
    print("TITIK PENGAWAS: kuadran", " ".join(map(str, kuadran_arr)))
    print("KEJAR BJARKAN!!!, Dia Masih Segaris Dengan Kalian")