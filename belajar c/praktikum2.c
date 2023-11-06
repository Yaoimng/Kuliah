#include<stdio.h>
#include<string.h>

// int main()
//     {
//         int a;
//         printf("Masukkan Nilai Ujian : ");
//         scanf("%d", &a);
//         if (a >= 70)
//         {
//             printf("Anda Lulus \n");
//         }
//         else
//         {
//             printf("Anda Tidak Lulus\n");
//         }
//         printf("Masukkan Nilai Ujian : ");
//         scanf("%d", &a);
//         if (a >= 70)
//         {
//             printf("Anda Lulus \n");
//         }
//         else
//         {
//             printf("Anda Tidak Lulus\n");
//         }        
//         return 0;
//     }   

// int main()
// {
//     int x;
//     printf("Hari ke...: ");
//     scanf("%d", &x);
//     if (x == 1){
//         printf("Minggu");
//     }
//     else if (x == 2){
//         printf("Senin");
//     }
//     else if (x == 3){
//         printf("Selasa");
//     }
//     else if (x == 4){
//         printf("Rabu");
//     }
//     else if (x == 5){
//         printf("Kamis");
//     }
//     else if (x == 6){
//         printf("Jum'at");
//     }
//     else if (x == 7){
//         printf("Sabtu");
//     }
//     else
//     {
//         printf("Tidak valid");
//     }
    

//         printf("\nHari ke...: ");
//     scanf("%d", &x);
//     if (x == 1){
//         printf("Minggu");
//     }
//     else if (x == 2){
//         printf("Senin");
//     }
//     else if (x == 3){
//         printf("Selasa");
//     }
//     else if (x == 4){
//         printf("Rabu");
//     }
//     else if (x == 5){
//         printf("Kamis");
//     }
//     else if (x == 6){
//         printf("Jum'at");
//     }
//     else if (x == 7){
//         printf("Sabtu");
//     }
//     else{
//     printf("Tidak valid");
//     }
//     return 0;
// }

// int main()
// {
//     int suhu;
//     printf("Masukkan suhu dalam celcius : ");
//     scanf("%d", &suhu);
//     if (suhu >= 30)
//     {
//         printf("Suhu sangat panas");
//     }
//     else if (suhu <= 0)
//     {
//         printf("Suhu sangat dingin");
//     }
//     else
//     {
//         printf("Suhu sangat sejuk");
//     }  
// }

int main(){
    char huruf;
    int angka;
    printf("Masukkan nilai huruf : ");
    scanf("%c", &huruf);
    switch (huruf)
    {
    case 'A':   
        angka = 4;
        printf("Nilai angka : %d", angka);
        break;
    case 'B':
        angka = 3;
        printf("Nilai angka : %d", angka);
        break;
    case 'C':
        angka = 2;
        printf("Nilai angka : %d", angka);
        break;
    case 'D':
        angka = 1;
        printf("Nilai angka : %d", angka);
        break;
    case 'E':
        angka = 0;
        printf("Nilai angka : %d", angka);
        break; 
    default:
        break;
    }
}

// int main(){
//     int a, b, c, result;
//     printf("Masukkan 3 angka : ");
//     scanf("%d %d %d", &a, &b, &c);
//     if (a<b){
//         if (a<c)
//         {
//             result = a;
//             printf("Angka yang terkecil adalah %d", result);
//         }
//         else
//         {
//             result = c;
//             printf("Angka yang terkecil adalah %d", result);
//         }
//     }
//     else if (b<c){
//         result = b;
//         printf("Angka yang terkecil adalah %d", result);}
//     else{
//         result = c;
//         printf("Angka yang terkecil adalah %d", result);}   
// }

// int main(){
//     int pemakaian, biaya, kwh;
//     printf("Masukkan pemakaian rekening listrik : ");
//     scanf("%d", &pemakaian);
//     if (pemakaian <= 100)
//     {
//         biaya = 100000;
//         printf("Biaya pemakaian %d", biaya);
//     }
//     else if (pemakaian >100 && pemakaian <=500)
//     {
//         kwh = pemakaian - 100;
//         biaya = 100000 + (1500 * kwh);
//         printf("Biaya pemakaian %d", biaya);
//     }
//     else if (pemakaian >500){
//         kwh = pemakaian - 500;
//         biaya = 700000 + (2000 * kwh);
//         printf("Biaya pemakaian %d", biaya);
//     }
// }
