#1
SELECT ID_transaksi, Tanggal_transaksi FROM Transaksi
WHERE Tanggal_transaksi BETWEEN '2023-10-10' AND '2023-10-20';

#2
SELECT t.ID_transaksi, SUM(m.harga_minuman * tm.jumlah_minuman) AS TOTAL_HARGA
FROM Transaksi t
JOIN Transaksi_minuman tm ON t.ID_transaksi = tm.tm_transaksi_id
JOIN Menu_minuman m ON tm.tm_menu_minuman_id = m.id_minuman
GROUP BY t.ID_transaksi;

#3
SELECT c.*, SUM(m.harga_minuman * tm.jumlah_minuman) AS Total_Belanja
FROM Customer c
JOIN transaksi t ON c.id_customer = t.customer_id_customer
JOIN transaksi_minuman tm ON t.id_transaksi = tm.tm_transaksi_id
JOIN menu_minuman m ON tm.tm_menu_minuman_id = m.id_minuman
WHERE t.tanggal_transaksi BETWEEN '2023-10-03' AND '2023-10-22'
GROUP BY c.ID_customer
ORDER BY c.nama_customer ASC;

#4
SELECT c.nama_customer AS Customer, p.nama_pegawai FROM pegawai p
JOIN transaksi t ON p.nik = t.pegawai_nik
JOIN customer c ON t.customer_id_customer = c.id_customer
WHERE c.nama_customer IN ('Davi Liam', 'Sisil Triana', 'Hendra Astro');

#5
SELECT YEAR(t.tanggal_transaksi) AS TAHUN, MONTH(t.tanggal_transaksi) AS BULAN,
SUM(tm.jumlah_minuman) AS JUMLAH_CUP
FROM transaksi t
JOIN transaksi_minuman tm ON t.id_transaksi = tm.tm_transaksi_id
JOIN menu_minuman m ON tm.tm_menu_minuman_id = m.id_minuman
GROUP BY TAHUN, BULAN
ORDER BY TAHUN DESC, BULAN ASC;

#6
SELECT AVG(total_belanja) AS RATA_RATA_TOTAL_BELANJA
FROM (SELECT  c.id_customer, SUM(m.harga_minuman * tm.jumlah_minuman) AS total_belanja
FROM customer c
JOIN membership mb ON c.id_customer = mb.m_id_customer
JOIN transaksi t ON c.id_customer = t.customer_id_customer
JOIN transaksi_minuman tm ON t.id_transaksi = tm.tm_transaksi_id
JOIN menu_minuman m ON tm.tm_menu_minuman_id = m.id_minuman
GROUP BY c.id_customer, t.id_transaksi) AS total_belanja_per_customer;