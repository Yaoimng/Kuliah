CREATE TABLE Kategori(
  kid integer PRIMARY KEY,
  Genre varchar(10)
);

CREATE TABLE Film (
  fid integer PRIMARY KEY,
  fjudul varchar(20),
  ftahun char(4),
  f_k_id integer,
  FOREIGN KEY (f_k_id) REFERENCES Kategori(kid)
);

CREATE TABLE Aktor(
  aid integer PRIMARY KEY,
  anama varchar(10),
  akota_lahir varchar(10),
  atahun_lahir char(4)
);

CREATE TABLE Membintangi(
  mid integer PRIMARY KEY,
  m_f_id integer,
  m_a_id integer,
  FOREIGN KEY (m_f_id) REFERENCES Film(fid),
  FOREIGN KEY (m_a_id) REFERENCES Aktor(aid)
);

INSERT INTO Kategori (kid, Genre) VALUES (101, 'Horor');
INSERT INTO Kategori (kid, Genre) VALUES (102, 'Anime');
INSERT INTO Kategori (kid, Genre) VALUES (103, 'Rom');
INSERT INTO Kategori (kid, Genre) VALUES (104, 'Com');
INSERT INTO Kategori (kid, Genre) VALUES (105, 'Fantasi');
INSERT INTO Kategori (kid, Genre) VALUES (106, 'Drama');
INSERT INTO Kategori (kid, Genre) VALUES (107, 'Aksi');
INSERT INTO Kategori (kid, Genre) VALUES (108, 'Fiksi');
INSERT INTO Kategori (kid, Genre) VALUES (109, 'Petualang');
INSERT INTO Kategori (kid, Genre) VALUES (110, 'Thriller');

INSERT INTO FIlm (fid, fjudul, ftahun,f_k_id) VALUES (111, 'TItanic','1997',103);
INSERT INTO FIlm (fid, fjudul, ftahun,f_k_id) VALUES (112, 'Dark','2016',105);
INSERT INTO FIlm (fid, fjudul, ftahun,f_k_id) VALUES (113, 'Fnaf','2023',101);
INSERT INTO FIlm (fid, fjudul, ftahun,f_k_id) VALUES (114, 'Loki','2021',105);
INSERT INTO FIlm (fid, fjudul, ftahun,f_k_id) VALUES (115, 'JJK','2020',102);
INSERT INTO FIlm (fid, fjudul, ftahun,f_k_id) VALUES (116, 'SaWX','2023',110);
INSERT INTO FIlm (fid, fjudul, ftahun,f_k_id) VALUES (117, 'The nun','2019',101);
INSERT INTO FIlm (fid, fjudul, ftahun,f_k_id) VALUES (118, 'Megan','2022',101);
INSERT INTO FIlm (fid, fjudul, ftahun,f_k_id) VALUES (119, 'Hill House','2019',101);
INSERT INTO FIlm (fid, fjudul, ftahun,f_k_id) VALUES (120, 'Indiana J','2023',107);

INSERT INTO Aktor (aid, anama, akota_lahir, atahun_lahir) VALUES (121, 'Leonardo','LA','1983');
INSERT INTO Aktor (aid, anama, akota_lahir, atahun_lahir) VALUES (122, 'Andi','New York','1993');
INSERT INTO Aktor (aid, anama, akota_lahir, atahun_lahir) VALUES (123, 'Michael','Ngawi','2003');
INSERT INTO Aktor (aid, anama, akota_lahir, atahun_lahir) VALUES (124, 'Jony','Malang','1995');
INSERT INTO Aktor (aid, anama, akota_lahir, atahun_lahir) VALUES (125, 'Jason','Jakarta','1995');
INSERT INTO Aktor (aid, anama, akota_lahir, atahun_lahir) VALUES (126, 'Niko','Cambridge','1934');
INSERT INTO Aktor (aid, anama, akota_lahir, atahun_lahir) VALUES (127, 'David','UK','1900');
INSERT INTO Aktor (aid, anama, akota_lahir, atahun_lahir) VALUES (128, 'Mei','Stuttgart','1910');
INSERT INTO Aktor (aid, anama, akota_lahir, atahun_lahir) VALUES (129, 'Casey','Berlin','1923');
INSERT INTO Aktor (aid, anama, akota_lahir, atahun_lahir) VALUES (130, 'Ben','New Jersey','2000');

INSERT INTO Membintangi (mid, m_f_id, m_a_id) VALUES (131, 112, 126);
INSERT INTO Membintangi (mid, m_f_id, m_a_id) VALUES (132, 111, 122);
INSERT INTO Membintangi (mid, m_f_id, m_a_id) VALUES (133, 119, 124);
INSERT INTO Membintangi (mid, m_f_id, m_a_id) VALUES (134, 116, 121);
INSERT INTO Membintangi (mid, m_f_id, m_a_id) VALUES (135, 114, 129);
INSERT INTO Membintangi (mid, m_f_id, m_a_id) VALUES (136, 115, 128);
INSERT INTO Membintangi (mid, m_f_id, m_a_id) VALUES (137, 117, 127);
INSERT INTO Membintangi (mid, m_f_id, m_a_id) VALUES (138, 113, 125);
INSERT INTO Membintangi (mid, m_f_id, m_a_id) VALUES (139, 114, 127);
INSERT INTO Membintangi (mid, m_f_id, m_a_id) VALUES (140, 120, 130);

UPDATE Aktor SET anama='Fadhil' WHERE aid=127;
UPDATE Aktor SET anama='Razzan' WHERE aid=122;
UPDATE Film SET fjudul='Ice Cold' WHERE fid=117;
UPDATE Film SET ftahun='2014' WHERE fid=112;
UPDATE Film SET ftahun='2002' WHERE fid=119;
UPDATE Kategori SET Genre='Horor' WHERE kid=102;
UPDATE Kategori SET Genre='Anime' WHERE kid=101;
UPDATE Kategori SET Genre='Thriller' WHERE kid=110;
UPDATE Aktor SET akota_lahir='Madiun' WHERE aid=124;
UPDATE Aktor SET atahun_lahir='2004' WHERE aid=127;
UPDATE Aktor SET atahun_lahir='1995' WHERE aid=125;

DELETE FROM Membintangi WHERE mid=140;
DELETE FROM Film WHERE fid=120;
DELETE FROM Aktor WHERE aid=130;
DELETE FROM Aktor WHERE anama='Ben';
DELETE FROM Membintangi Where mid=139;

SELECT * FROM Kategori
SELECT * FROM Film
SELECT * FROM Aktor
SELECT * FROM Membintangi