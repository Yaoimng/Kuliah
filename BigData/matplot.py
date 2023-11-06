import matplotlib.pyplot as plt

x = [2000, 2001,2002, 2003, 2004, 2005]
y = [11, 22, 100, 45, 10, 25]

plt.bar(x, y, color='green', label='data')
plt.xlabel('Tahun')
plt.ylabel('Mobil')
plt.title('Grafik mobil tahunan')
plt.legend()
plt.grid()
plt.show()