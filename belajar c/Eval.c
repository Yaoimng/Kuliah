#include<stdio.h>
#include<string.h>

int main()
    {
        int a,b = 900;
        do
        {
            printf("Masukkan Tebakan anda : ");
        scanf("%d", &a);
        if (a > b )
        {
            printf("Lebih kecil \n");
        }
        if (a < b)
        {
            printf("Lebih besar \n");
        }
        } while (a != b);
        printf("Selamat!");
        return 0;
    }   

// #include <stdio.h>

// // Fungsi untuk mengonversi angka analog ke digital
// void analogToDigital(int angka, char digital[]) {
//     int i;
//     for (i = 0; i < 8; i++) {
//         if (angka % 2 == 0) {
//             digital[7 - i] = '0'; // Mengisi array dengan '0' jika angka genap
//         } else {
//             digital[7 - i] = '1'; // Mengisi array dengan '1' jika angka ganjil
//         }
//         angka /= 2;
//     }
//     digital[8] = '\0'; // Menambahkan karakter null terminator pada akhir string
// }

// int main() {
//     int angka;
//     char digital[9]; // Array untuk menyimpan hasil konversi

//     printf("Masukkan angka analog (0 - 255): ");
//     scanf("%d", &angka);

//     if (angka >= 0 && angka <= 255) { // Memeriksa apakah angka berada dalam rentang yang valid
//         analogToDigital(angka, digital);
//         printf("Angka digital (8 bit): %s\n", digital);
//     } else {
//         printf("Angka tidak valid!\n");
//     }

//     return 0;
// }