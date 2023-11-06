plt = input()
plt_arr = plt.split(' ')

x = int(plt_arr[0])
y = int(plt_arr[1])
z = int(plt_arr[2])

if x + y > z and x + z > y and y + z > x:
    print('Tri-force dapat terbentuk!')
else:
    print('Tri-force gagal terbentuk :(')