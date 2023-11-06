import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import date

# Membuat atau menghubungkan ke database
conn = sqlite3.connect("kasir.db")
cursor = conn.cursor()

# Membuat tabel Penjualan, Pembelian, dan Persediaan
cursor.execute('''CREATE TABLE IF NOT EXISTS Penjualan
                  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   Tanggal DATE,
                   NamaBarang TEXT,
                   Jumlah INTEGER,
                   Harga FLOAT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Pembelian
                  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   Tanggal DATE,
                   NamaBarang TEXT,
                   Jumlah INTEGER,
                   Harga FLOAT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Persediaan
                  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   NamaBarang TEXT,
                   Stok INTEGER,
                   Harga FLOAT)''')

# Fungsi untuk menyimpan data penjualan
def simpan_penjualan():
    try:
        nama_barang = nama_barang_entry.get()
        jumlah = int(jumlah_entry.get())
        harga = float(harga_entry.get())
        tanggal = date.today()
        
        if nama_barang and jumlah > 0 and harga > 0:
            cursor.execute("INSERT INTO Penjualan (Tanggal, NamaBarang, Jumlah, Harga) VALUES (?, ?, ?, ?)",
                           (tanggal, nama_barang, jumlah, harga))
            
            conn.commit()
            messagebox.showinfo("Sukses", "Data penjualan berhasil disimpan.")
            
            # Update stok persediaan
            cursor.execute("SELECT Stok FROM Persediaan WHERE NamaBarang=?", (nama_barang,))
            row = cursor.fetchone()
            if row:
                stok = row[0]
                stok -= jumlah
                cursor.execute("UPDATE Persediaan SET Stok=? WHERE NamaBarang=?", (stok, nama_barang))
                conn.commit()
                tampilkan_stok_persediaan()
            else:
                messagebox.showwarning("Peringatan", "Nama barang tidak ditemukan dalam persediaan.")
        else:
            messagebox.showwarning("Peringatan", "Harap isi semua kolom dengan benar.")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Kesalahan", f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk menampilkan data penjualan di daftar
def tampilkan_data_penjualan():
    daftar_penjualan.delete(*daftar_penjualan.get_children())
    cursor.execute("SELECT * FROM Penjualan")
    data_penjualan = cursor.fetchall()
    for item in data_penjualan:
        daftar_penjualan.insert("", "end", values=item)

# Fungsi untuk menampilkan stok persediaan di daftar
def tampilkan_stok_persediaan():
    daftar_persediaan.delete(*daftar_persediaan.get_children())
    cursor.execute("SELECT * FROM Persediaan")
    data_persediaan = cursor.fetchall()
    for item in data_persediaan:
        daftar_persediaan.insert("", "end", values=item)

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Aplikasi Kasir")

# Membuat elemen-elemen GUI
frame_input = ttk.Frame(app)
frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="w")

frame_penjualan = ttk.Frame(app)
frame_penjualan.grid(row=0, column=1, padx=10, pady=10, sticky="e")

nama_barang_label = ttk.Label(frame_input, text="Nama Barang:")
nama_barang_entry = ttk.Entry(frame_input)
jumlah_label = ttk.Label(frame_input, text="Jumlah:")
jumlah_entry = ttk.Entry(frame_input)
harga_label = ttk.Label(frame_input, text="Harga:")
harga_entry = ttk.Entry(frame_input)
simpan_button = ttk.Button(frame_input, text="Simpan Penjualan", command=simpan_penjualan)

daftar_penjualan = ttk.Treeview(frame_penjualan, columns=("ID", "Tanggal", "Nama Barang", "Jumlah", "Harga"))
daftar_penjualan.heading("#1", text="ID")
daftar_penjualan.heading("#2", text="Tanggal")
daftar_penjualan.heading("#3", text="Nama Barang")
daftar_penjualan.heading("#4", text="Jumlah")
daftar_penjualan.heading("#5", text="Harga")
tampilkan_data_penjualan()

frame_persediaan = ttk.Frame(app)
frame_persediaan.grid(row=1, column=0, padx=10, pady=10, sticky="w")

daftar_persediaan = ttk.Treeview(frame_persediaan, columns=("ID", "Nama Barang", "Stok", "Harga"))
daftar_persediaan.heading("#1", text="ID")
daftar_persediaan.heading("#2", text="Nama Barang")
daftar_persediaan.heading("#3", text="Stok")
daftar_persediaan.heading("#4", text="Harga")
tampilkan_stok_persediaan()

# Mengatur tata letak elemen-elemen GUI
nama_barang_label.grid(row=0, column=0, sticky="e")
nama_barang_entry.grid(row=0, column=1, padx=5, pady=5)
jumlah_label.grid(row=1, column=0, sticky="e")
jumlah_entry.grid(row=1, column=1, padx=5, pady=5)
harga_label.grid(row=2, column=0, sticky="e")
harga_entry.grid(row=2, column=1, padx=5, pady=5)
simpan_button.grid(row=3, columnspan=2, pady=10)

daftar_penjualan.grid(row=0, column=0)
daftar_persediaan.grid(row=0, column=0)

# Jalankan aplikasi
app.mainloop()

# Tutup koneksi ke database saat aplikasi selesai
conn.close()
