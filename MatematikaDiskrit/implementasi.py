def insertsort_train_schedule(train_schedule):
    n = len(train_schedule)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if train_schedule[j][1] < train_schedule[j - 1][1]:
                train_schedule[j], train_schedule[j - 1] = train_schedule[j - 1], train_schedule[j]

# Inputan jadwal kereta
train_schedule_input = []
try:
    num_trains = int(input("Masukkan jumlah jadwal kereta: "))
except ValueError:
    print("Input harus berupa bilangan bulat.")
    exit()
    
for i in range(num_trains):
    train_name = input(f"Masukkan nama kereta ke-{i + 1}: ")
    while True:
        arrival_time = input(f"Masukkan waktu kedatangan kereta {train_name} (format HH:mm): ")
        try:
            hours, minutes = map(int, arrival_time.split(':'))
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                break
            else:
                print("format waktu valid")
        except ValueError:
            print("Format waktu tidak valid")
    train_schedule_input.append((train_name, arrival_time))

# Panggil fungsi pengurutan
insertsort_train_schedule(train_schedule_input)

# Tampilkan jadwal kereta setelah pengurutan
print("\nJadwal kedatangan kereta yang diurutkan:")
for train in train_schedule_input:
    print(f"{train[0]} - {train[1]}")
