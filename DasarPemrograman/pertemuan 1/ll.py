import datetime

n = input()
n_arr = n.split(' ')

year = int(n_arr[2])
month = int(n_arr[1])
day = int(n_arr[0])


day = datetime.date(year, month, day).weekday()
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat","Sabtu", "Minggu"]
print(hari[day])