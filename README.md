# 🏎️ Karting Deng

![Unity](https://img.shields.io/badge/Unity-2021.3%2B-black?style=flat&logo=unity)
![Language](https://img.shields.io/badge/Language-C%23-blue?style=flat&logo=csharp)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

**Karting Deng** adalah sebuah game balap arcade *fast-paced* yang dikembangkan menggunakan **Unity Engine**. Proyek ini merupakan kustomisasi dan pengembangan lebih lanjut dari *Unity Karting Microgame*, menampilkan desain sirkuit orisinil (custom map), visual low-poly yang unik, dan implementasi logika AI berbasis checkpoint.

---

## 📸 Galeri / Screenshot

| Main Menu | Gameplay |
| :---: | :---: |
| <img width="958" height="538" alt="image" src="https://github.com/user-attachments/assets/7a9b4c02-5358-412f-a88c-908c4d3b6a84" /> | (<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/84a9fcc9-7807-4648-b765-e2d91cb3d401" />) |

| Map Overview | Environment |
| :---: | :---: |
| (<img width="1036" height="532" alt="image" src="https://github.com/user-attachments/assets/d50d7b5d-56f9-414a-92ff-5fe53c675dbb" /> | (<img width="1036" height="533" alt="image" src="https://github.com/user-attachments/assets/b6d6f081-ff8c-483b-a083-bc5075a94b81" />) |

> *Visual game menampilkan estetika low-poly dengan pencahayaan bergaya synthwave/sunset.*

---

## 🎮 Tentang Proyek

Game ini dibuat dengan fokus pada desain level (Level Design) dan pemrograman logika navigasi sederhana untuk NPC. Pemain ditantang untuk menyelesaikan satu putaran (lap) penuh pada sirkuit custom yang penuh tikungan tajam dan rintangan, bersaing melawan agen AI.

### Fitur Utama
* **Custom Map Design**: Peta/sirkuit tidak menggunakan *preset* bawaan, melainkan dibangun secara manual (*hand-crafted*) menggunakan aset modular untuk menciptakan alur balapan yang unik, termasuk jembatan *overpass* dan tikungan tajam.
* **Checkpoint-Based AI Navigation**: Lawan (NPC/ML Agent) tidak hanya bergerak acak. Mereka diprogram untuk mendeteksi serangkaian *Collider Checkpoint* yang saya tempatkan secara strategis di sepanjang peta buatan saya. AI akan mengejar checkpoint berikutnya secara berurutan hingga garis finis.
* **Sistem Game Loop**: Implementasi logika *Win/Loss* sederhana di mana permainan berakhir (Game Over/Finish) setelah menyelesaikan 1 Lap penuh.
* **Estetika Visual**: Pengaturan *Lighting* dan *Skybox* yang disesuaikan untuk menciptakan nuansa sore hari yang hangat dan vibrant.

---

## 🕹️ Kontrol (Keyboard)

Game ini dirancang untuk dimainkan menggunakan Keyboard pada PC:

* **W / Panah Atas**: Gas (Akselerasi)
* **S / Panah Bawah**: Rem / Mundur
* **A / D atau Panah Kiri/Kanan**: Menyetir (Steering)
* **Spasi**: Drift / Rem Tangan
* **Tab**: Pause Menu

---

## 🛠️ Teknologi yang Digunakan

* **Game Engine**: Unity (LTS Version)
* **Bahasa Pemrograman**: C#
* **Assets**: Unity Asset Store (Karting Microgame Foundation)
* **Tools**: Visual Studio / VS Code

---

## 📂 Struktur Pengembangan

1.  **Map Creation**: Menyusun aset jalan, gedung, dan terrain untuk membuat sirkuit tertutup.
2.  **Logic Implementation**: Menambahkan *Collider* tak terlihat (invisible colliders) sebagai trigger untuk AI dan penghitung progres Lap pemain.
3.  **UI Integration**: Kustomisasi Main Menu dan HUD (Timer, Lap Count).

---

## 📝 Credits

* **Developer**: [Nama Kamu/Username GitHub]
* **Base Assets**: Unity Technologies (Karting Microgame)

---

*Terima kasih telah mengunjungi repositori ini! Jangan ragu untuk memberikan bintang (⭐) jika Anda menyukai proyek ini.*
