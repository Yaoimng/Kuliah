#include <stdio.h>

// int main() {
//     int m, n;
//     char huruf = 'A';
//     printf("Masukkan Jumlah baris: ");
//     scanf("%d", &m);
//     printf("Masukkan Jumlah kolom: ");
//     scanf("%d", &n);
//     int i, j;
//     for (i = 0; i < m; i++) {
//         for (j = 0; j < n; j++) {
//           printf("%c ", huruf);
//         }
//     printf("\n");
//     }

//     return 0;
// }
#include <stdio.h>

// int main() {
//     int i, j;
//     for (i = 0; i < 4; i++) {
//         for (j = 0; j < 3; j++) {
//             printf("* ");
//         }
//         for (j = 0; j < 3; j++) {
//             printf("- ");
//         }
//     printf("\n");
//     }
//   return 0;
// }

// #include <stdio.h>

// int main() {
//     int n, i, j;
//     printf("Masukkan nilai n: ");
//     scanf("%d", &n);
//     for (i = 1; i <= n; i++) {
//         for (j = 1; j <= n-i; j++) {
//             printf(" ");
//         }
//         for (j = 1; j <= i; j++) {
//             printf("*");
//         }
//         printf("\n");
//     }
//     for (i = n-1; i >= 1; i--) {
//         for (j = 1; j <= n-i; j++) {
//             printf(" ");
//         }
//         for (j = 1; j <= i; j++) {
//             printf("*");
//         }
//         printf("\n");
//     }
//     return 0;
// }

#include <stdio.h>

// int main() {
//     int baris = 3;
//     int kolom = 5;
//     for (int i = 1; i <= baris; i++) {
//         for (int j = 1; j <= kolom; j++) {
//             int value = i * j;
//             printf("%d ", value);
//         }
//         printf("\n");
//     }
//     return 0;
// }

#include <stdio.h>

// int main() {
//    int n, i;
//    float nilai, total = 0, rata;

//    printf("Banyaknya data? ");
//    scanf("%d", &n);

//    for (i = 1; i <= n; i++) {
//       printf("Data ke %d? ", i);
//       scanf("%f", &nilai);

//       if (nilai < 0) {
//          printf("Nilai tidak valid. Silakan masukkan nilai yang valid.\n");
//          i--;
//          continue;
//       }

//       total += nilai;
//    }

//    rata = total / n;
//     printf("banyaknya mahasiswa = %d\n",n );
//    printf("Total nilai: %f\n", total);
//    printf("Rata-rata nilai: %f\n", rata);

//    return 0;
// }

#include <stdio.h>

// int main() {
//    int B = 0;
//    printf("Masukkan nilai B: ");
//    scanf("%d", &B);
//    if (B == 0) {
//       goto Tak_berhingga;
//    }
//    printf("Nilai B adalah %d dan bukan 0\n", B);
//    return 0;
//    Tak_berhingga:
//    printf("Nilai B adalah 0. Tak berhingga\n");
//    return 0;
// }

#include <stdio.h>

int main() {
    int m, i, j, n = 2, count = 0, sum = 0;
    printf("Masukkan nilai M: ");
    scanf("%d", &m);

    printf("Bilangan prima yang ke ");
    for (i = 1; i <= m; i++) {
        int isPrime = 1;
        for (j = 2; j <= n / 2; j++) {
            if (n % j == 0) {
                isPrime = 0;
                break;
            }
        }
        if (isPrime) {
            count++;
            printf("%d = %d\n", count, n);
            sum += n;
        } else {
            i--;
        }
        n++;
    }
    printf("Total bilangan prima pertama = %d", sum);

    return 0;
}


