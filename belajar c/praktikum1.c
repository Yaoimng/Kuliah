//Percobaan 1

#include<stdio.h>
#include<string.h>

// int main(){
//     char Nama[15];
//     char Umur[15];
//     char no[15];
//     printf("Masukkan data diri anda");
//     printf("\n Nama : ");
//     scanf("%s", &Nama);
//     printf("\n Umur : ");
//     scanf("%s", &Umur);
//     printf("\n No. Telfon: ");
//     scanf("%s", &no);
//     printf("\n Hello %s, umur %s, no telp %s\n", &Nama, &Umur, &no);
//     printf("Bagaimana kabar anda hari ini?");
// }

// int main(){
//     int Kecepatan, Waktu, Jatem;
//     printf("Masukkan kecepatan dan waktu mobil anda");
//     printf("\n Kecepatan (m/detik): ");
//     scanf("%d", &Kecepatan);
//     printf("\n Waktu (detik): ");
//     scanf("%d", &Waktu);

//     Jatem = Kecepatan * Waktu;

//     printf("Jadi jarak tempuh(m) anda adalah %d meter", Jatem);
// }

// int main(){
//     int a, b, c;
//     printf("Masukkan bilangan pertama : \n");
//     scanf("%d", &a);
//     printf("Masukkan bilangan kedua : \n");
//     scanf("%d", &b);

//     c = a;
//     a = b;
//     b = c;

//     printf("jadi bilangan pertama sekarang %d", a);
//     printf("\n jadi bilangan kedua sekarang %d", b);
// }

int main(){
    int panjang, lebar, tinggi, volume;
    printf("Masukkan panjang, lebar, dan tinggi : \n");
    printf("Panjang(cm): ");
    scanf("%d", &panjang);
    printf("lebar(cm): ");
    scanf("%d", &lebar);
    printf("Tinggi(cm): ");
    scanf("%d", &tinggi);

    volume = panjang * lebar * tinggi;

    printf("Jadi volumenya adalah %d cm kubik", volume);
}

// int main()
// {   
//     int opsi;
//     printf("Pilih\n");
//     printf("1. Data Diri\n");
//     printf("2. Jarak Tempuh\n");
//     printf("3. Tukar Nilai\n");
//     printf("4. Volume Kotak\n");
//     scanf("%d", &opsi);

//     switch (opsi)
//     {
//     case 1:
//         Data_diri();
//         break;
//     case 2:
//         jarak_tempuh();
//         break;
//     case 3:
//         tukar_nilai();
//         break;
//     case 4:
//         volume_kotak();
//         break;
    
//     default:
//         printf("Pilih tidak valid\n");
//         break;
//     }
//     return 0;
// }