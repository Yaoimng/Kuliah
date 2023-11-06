CREATE TABLE Karyawan (
    ID INT PRIMARY KEY,
    Nama VARCHAR(50),
    Alamat VARCHAR(100),
    Gaji DECIMAL(10, 2),
    Tanggal_Masuk DATE,
    Depart_ID INT,
    FOREIGN KEY (Depart_ID) REFERENCES Depart(ID)
);

CREATE TABLE Depart (
    ID INT PRIMARY KEY,
    Nama VARCHAR(50),
    Lokasi VARCHAR(50)
);

-- Sisipkan data depart baru
INSERT INTO Depart (ID, Nama, Lokasi)
VALUES (1, 'Keuangan', 'Gedung A, Lantai 2');   

INSERT INTO Depart (ID, Nama, Lokasi)
VALUES (2, 'Teknologi Informasi', 'Gedung B, Lantai 3');

INSERT INTO Depart (ID, Nama, Lokasi)
VALUES (3, 'Sumber Daya Manusia', 'Gedung C, Lantai 1');


-- Sisipkan data karyawan baru
INSERT INTO Karyawan (ID, Nama, Alamat, Gaji, Tanggal_Masuk, Depart_ID)
VALUES (1, 'John Doe', 'Jl. Contoh No. 123', 50000.00, '2023-01-15', 1);

INSERT INTO Karyawan (ID, Nama, Alamat, Gaji, Tanggal_Masuk, Depart_ID)
VALUES (2, 'Jane Smith', 'Jl. Contoh No. 456', 60000.00, '2022-11-10', 2);

-- Ambil semua data karyawan
SELECT * FROM Karyawan;

-- Ambil data karyawan dengan gaji di atas 55000
SELECT * FROM Karyawan WHERE Gaji > 55000;

-- Ambil data karyawan dari depart tertentu (misalnya Depart_ID = 2)
SELECT * FROM Karyawan WHERE Depart_ID = 2;

-- Ambil data karyawan dengan nama tertentu (misalnya "John Doe")
SELECT * FROM Karyawan WHERE Nama = 'John Doe';
