#include<stdio.h>
#include<stdlib.h>
#include<time.h>

// int main()
// {
//     int bilangan, pembagi, sisa;
//     char pilihan;
//     do
//     {
//         printf("Masukkan suatu bilangan: ");
//         scanf("%d", &bilangan);
//         printf("Masukkan bilangan pembagi: ");
//         scanf("%d", &pembagi);
//         sisa = bilangan % pembagi;
//         if (sisa == 0)
//         {
//             printf("Sisa bagi : tidak ada");
//         }
//         else
//         {
//             printf("Sisa bagi : %d", sisa);
//         }
//         printf("\nApakah anda ingin meneruskanan: (y/t) ");
//         scanf(" %c", &pilihan);
//     } while (pilihan == 'y' || pilihan == 'Y');
//     return 0;
// }

// int main()
// {
//     int positif, jumlah;
//     printf("Masukkan integer positif : ");
//     scanf("%d", &positif);
//     int i;
//     for ( i = 1; i <= positif; i++)
//     {
//         jumlah += i;
//     }
//     printf("\nJumlah 1 sampai %d = %d", positif,jumlah);
//     return 0;
// }

// int main()
// {
//     int bilangan, total = 0,i = 1;
//     char pilihan = 'y';
//     while (pilihan == 'y' || pilihan == 'Y')
//     {   
//         printf("Masukkan Bilangan ke-%d : ", i);
//         scanf("%d", &bilangan);
//         printf("Mau memasukkan data lagi [y/t]?");
//         scanf(" %c", &pilihan);
//         total += bilangan;
//         i++;
//     }
//     printf("Total bilangan : %d\n", total);
//     return 0;
// }

// int main() {
//     int angkaAcak, tebakan;
//     srand(time(0)); 
//     angkaAcak = rand() % 100 + 1; 
//     do {
//         printf("Angka tebakan: ");
//         scanf("%d", &tebakan);
//         if (tebakan < angkaAcak) {
//             printf("Tebakan terlalu kecil\n");
//         } else if (tebakan > angkaAcak) {
//             printf("Tebakan terlalu besar\n");
//         }
//     } while (tebakan != angkaAcak);
//     printf("Angka tebakan: %d\n", angkaAcak);
//     printf("Tebakan benar\n");
//     return 0;
// }

int main() { 
  char jawaban;

  do {
    printf("Anda sudah sholat ? (s/b) ");
    scanf(" %c", &jawaban);
  } while (jawaban != 's' && jawaban != 'b');

  if (jawaban == 's') {
    printf("Bagus!\n");
  } else {
    printf("Sholat adalah ibadah\n");
  }

  return 0;
}