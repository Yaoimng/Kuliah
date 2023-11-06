#include<stdio.h>
#include<string.h>

// int main() //Percobaan array
// {
//     int mat, fis, kim, rata;
//     printf("Masukkan Nilai Matematika : ");
//     scanf("%d", &mat);
//     printf("Masukkan Nilai Fisika : ");
//     scanf("%d", &fis);
//     printf("Masukkan Nilai Kimia : ");
//     scanf("%d", &kim);
//     rata = (mat + fis + kim) / 3;

//     printf("Nilai rata-ratanya adalah : %d\n", rata); 

//     return 0;
// }

// #include <stdio.h>

// int main() {
//     char arr[26]; 
//     int freq[26] = {0}; 
//     int n, i;

//     printf("Masukkan jumlah karakter yang akan dihitung: ");
//     scanf("%d", &n);

//     for (i = 0; i < n; i++) {
//         printf("Masukkan karakter ke-%d: ", i+1);
//         scanf(" %c", &arr[i]);
//         freq[arr[i]-'a']++; 
//     }

//     for (i = 0; i < 26; i++) {
//         if (freq[i] > 0) {
//             printf("Frekuensi %c=%d\n", 'a'+i, freq[i]);
//         }
//     }
//     return 0;
// }

// #include <stdio.h>

// int main() {
//     int matrix1[2][3] = {{1, 2, 3}, {4, 5, 6}}; 
//     int matrix2[2][3] = {{7, 8, 9}, {10, 11, 12}}; 
//     int result[2][3]; 
//     int i, j;

//     for (i = 0; i < 2; i++) {
//         for (j = 0; j < 3; j++) {
//             result[i][j] = matrix1[i][j] + matrix2[i][j];
//         }
//     }

//     printf("Matriks hasil penjumlahan:\n");
//     for (i = 0; i < 2; i++) {
//         for (j = 0; j < 3; j++) {
//             printf("%d ", result[i][j]);
//         }
//         printf("\n");
//     }

//     return 0;
// }

// #include <stdio.h>

// int main() {
//     int n, i, j;
//     char nama[100][100];
//     int nilai[100][100];
//     float rata[100];

//     printf("Input jumlah mahasiswa: ");
//     scanf("%d", &n);

//     for (i = 0; i < n; i++) {
//         printf("Nama Mahasiswa-%d: ", i+1);
//         scanf("%s", &nama[i]);

//         printf("Jumlah nilai: ");
//         scanf("%d", &nilai[i][0]);

//         for (j = 1; j <= nilai[i][0]; j++) {
//             printf("Nilai-%d: ", j);
//             scanf("%d", &nilai[i][j]);
//         }
//     }

//     for (i = 0; i < n; i++) {
//         int total = 0;
//         for (j = 1; j <= nilai[i][0]; j++) {
//             total += nilai[i][j];
//         }
//         rata[i] = (float)total / nilai[i][0];
//         printf("Nilai rata-rata %s adalah %.2f.\n", nama[i], rata[i]);
//     }

//     return 0;
// }

#include <stdio.h>

int main() {
    int i, j, temp;
    int a, b, c;
    int bil[10];

    // input 10 bilangan dari keyboard
    for (i = 0; i < 10; i++) {
        printf("Masukkan bilangan ke-%d: ", i+1);
        scanf("%d", &bil[i]);
    }

    // sorting dengan metode bubble sort
    for (i = 0; i < 10; i++) {
        for (j = 0; j < 9-i; j++) {
            if (bil[j] < bil[j+1]) {
                temp = bil[j];
                bil[j] = bil[j+1];
                bil[j+1] = temp;
            }
        }
    }

    // tampilkan hasil sorting
    printf("Hasil pengurutan bilangan dari yang terbesar:\n");
    for (i = 0; i < 10; i++) {
        printf("%d ", bil[i]);
    }
    printf("\n");

    return 0;
}

